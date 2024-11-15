Passo a passo:

1. Gera o projeto: `django-admin startproject nome_do_projeto`. Vai criar uma pasta, dentro dela vai ter um manage.py e uma outra pasta com o mesmo nome.
2. Entra na pasta de fora
3. Cria uma aplicação específica: `python manage.py startapp nome_da_aplicacao`. Vai ficar assim:

```
meu_projeto/                  # Este é o diretório principal do projeto (não um aplicativo)
├── manage.py                 # Arquivo principal para executar comandos do Django
├── meu_projeto/              # Este diretório contém a configuração principal do projeto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Configurações do projeto (banco de dados, apps, etc.)
│   ├── urls.py               # Roteamento de URLs global do projeto
│   └── wsgi.py
└── projeto_estoque/          # Este é o diretório de um aplicativo, criado por você
    ├── __init__.py
    ├── admin.py
    ├── apps.py               # Arquivo de configuração do aplicativo
    ├── models.py             # Modelos de dados (Produto, Estoque, etc.)
    ├── migrations/           # Migrações para o banco de dados
    │   └── __init__.py
    ├── views.py              # Views relacionadas ao aplicativo
    └── urls.py               # Roteamento de URLs do aplicativo (se necessário)
```




# DAQUI PRA BAIXO TEM ALGUNS ERROS

# Estrutura de um projeto Django

Quando você cria um novo projeto Django usando o comando python -m django startproject <nome_do_projeto>, o Django gera uma estrutura inicial de arquivos e pastas para organizar seu projeto. Essa estrutura padrão ajuda a manter o projeto organizado e facilita o desenvolvimento.

Estrutura do projeto:
```shell
<nome_do_projeto>/
    ├── manage.py
    ├── <nome_do_projeto>/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## `<nome_do_projeto>/manage.py`

**Função**: manage.py é um script de linha de comando que facilita a administração do projeto Django.

Principais Comandos:

* python manage.py runserver: inicia o servidor de desenvolvimento.

* python manage.py migrate: aplica as migrações (alterações no banco de dados) necessárias.

* python manage.py createsuperuser: cria um usuário administrador para o painel de administração do Django.

* python manage.py startapp <nome_do_app>: cria uma nova aplicação Django dentro do projeto.


**Importância**: Ele configura o ambiente do Django, localizando o arquivo settings.py para carregar as configurações do projeto e executa comandos usando as funcionalidades do Django.

## `<nome_do_projeto>/<nome_do_projeto>/__init__.py`

**Função**: Este é um arquivo vazio que serve para indicar ao Python que essa pasta deve ser tratada como um pacote.

**Importância**: Torna a pasta <nome_do_projeto> (a segunda pasta com o nome do projeto) um pacote Python, permitindo que o projeto Django funcione como um módulo importável e que outros arquivos ou pacotes acessem as configurações e módulos.

## `<nome_do_projeto>/<nome_do_projeto>/settings.py`

**Função**: settings.py contém todas as configurações globais e específicas do projeto Django.

Principais Configurações:

* DEBUG: Define se o projeto está em modo de desenvolvimento (True) ou produção (False).
* INSTALLED_APPS: Lista todos os aplicativos Django ativos no projeto. Esses aplicativos podem ser internos (fornecidos pelo Django) ou externos (criados por você ou instalados de pacotes).
* DATABASES: Configurações do banco de dados, como tipo de banco (por exemplo, SQLite, PostgreSQL) e credenciais de acesso.
* MIDDLEWARE: Lista os middlewares, que são camadas de processamento entre o servidor e o código do projeto.
* TEMPLATES: Configurações para o sistema de templates, como localização dos arquivos de template e mecanismos de renderização.
* STATIC_URL e STATICFILES_DIRS: Define as configurações para os arquivos estáticos (CSS, JavaScript, imagens).
* ALLOWED_HOSTS: Lista os hosts/domínios autorizados para acesso ao projeto.

**Importância**: O arquivo settings.py centraliza as configurações do projeto, facilitando a administração e a modificação conforme o ambiente de execução (desenvolvimento, produção, etc.).

## `<nome_do_projeto>/<nome_do_projeto>/urls.py`

**Função**: urls.py é o arquivo onde você define as rotas (URLs) que mapeiam para diferentes views (páginas e funcionalidades) no projeto.

**Como Funciona**: Define um objeto urlpatterns, que é uma lista de caminhos (path() ou re_path()). Cada caminho especifica uma URL e a view (função ou classe) que deve ser executada ao acessar essa URL.

Exemplo de Conteúdo:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

**Importância**: Esse arquivo direciona as solicitações do usuário para as views apropriadas. Em projetos maiores, normalmente são configurados URLs principais que redirecionam para arquivos urls.py de cada app, organizando melhor o código.

## `<nome_do_projeto>/<nome_do_projeto>/asgi.py`

**Função**: asgi.py serve para configurar e inicializar o ASGI (Asynchronous Server Gateway Interface) do projeto.

**Importância**: Ele é necessário para implantar o projeto em servidores que suportam ASGI, oferecendo suporte para aplicativos assíncronos e comunicações em tempo real (WebSockets).

## `<nome_do_projeto>/<nome_do_projeto>/wsgi.py`

**Função**: wsgi.py configura o WSGI (Web Server Gateway Interface) para o projeto Django.

**Importância**: O arquivo é essencial para o deployment do projeto em produção, pois o WSGI é o protocolo padrão para servidores web interagirem com aplicativos Python, como o Django. Quando o projeto é implantado em um servidor WSGI, esse arquivo é utilizado para inicializar e fornecer o ambiente necessário.

Resumo

1. manage.py: Script principal de comando para gerenciamento do projeto (executar o servidor, aplicar migrações, etc.).

2. __init__.py: Indica que <nome_do_projeto> é um pacote Python.

3. settings.py: Armazena configurações gerais do projeto.

4. urls.py: Define as rotas e mapeamento das URLs para views.

5. asgi.py: Configuração para servidores assíncronos ASGI (recomendada para tempo real e websockets).

6. wsgi.py: Configuração para servidores WSGI (uso padrão em ambientes de produção com servidores web como Gunicorn, Apache).

Esses arquivos juntos formam a base inicial para um projeto Django, criando um ambiente organizado e modular. Essa estrutura permite adicionar novas funcionalidades e gerenciar o desenvolvimento de forma eficaz.


# Conectar no MySQL

Para conectar no banco de dados MySQL basta adicionar no arquivo `settings.py` o seguinte código no tópico já presente DATABASE:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Além disso, é preciso instalar o provider/driver de MySQL para o Python:

`pip install mysqlclient`

E também criar previamente o banco de dados.


