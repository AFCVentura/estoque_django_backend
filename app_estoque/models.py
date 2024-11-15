from django.db import models

# Create your models here.

class Estoque(models.Model):
    localizacao = models.CharField(
        max_length=100,  # Limite de 100 caracteres
        verbose_name="Localização",  # Nome amigável para exibição
        help_text="Localização do estoque (ex: 'Armazém A')"  # Descrição adicional
    )
    setor = models.CharField(
        max_length=100,
        verbose_name="Setor",
        help_text="Setor ou divisão do estoque (ex: 'Eletrônicos')"
    )

    def __str__(self):
        return f"{self.localizacao} - {self.setor}"  # Representação legível
    

class Produto(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome do Produto",
        help_text="Nome do produto (ex: 'Smartphone')"
    )
    descricao = models.TextField(
        verbose_name="Descrição",
        help_text="Descrição detalhada do produto"
    )
    quantidade_estoque = models.PositiveIntegerField(
        verbose_name="Quantidade em Estoque",
        help_text="Número total de unidades disponíveis"
    )
    preco = models.DecimalField(
        max_digits=10,  # Até 10 dígitos no total
        decimal_places=2,  # Com 2 casas decimais
        verbose_name="Preço",
        help_text="Preço do produto em reais (ex: '199.99')"
    )
    data_adicao = models.DateField(
        auto_now_add=True,  # Preenchido automaticamente no momento da criação
        verbose_name="Data de Adição",
        help_text="Data em que o produto foi adicionado"
    )
    estoque = models.ForeignKey(
        Estoque,  # Relacionamento com a entidade Estoque
        related_name='produtos',  # Nome para acessar produtos do estoque
        on_delete=models.CASCADE,  # Excluir produtos ao remover o estoque
        verbose_name="Estoque",
        help_text="Estoque em que o produto está armazenado"
    )

    def __str__(self):
        return self.nome
    
    