from django.shortcuts import render
from rest_framework import viewsets
from .models import Produto
from .models import Estoque
from .serializers import ProdutoSerializer
from .serializers import EstoqueSerializer

# Create your views here.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()  # Definindo a query para buscar todos os estoques
    serializer_class = EstoqueSerializer  # Definindo o serializer para a entidade Estoque