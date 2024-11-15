from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, EstoqueViewSet

# Criação do router
router = DefaultRouter()

# Registrando os ViewSets no router
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'estoques', EstoqueViewSet, basename='estoque')

# Incluindo as rotas geradas automaticamente pelo router
urlpatterns = [
    path('', include(router.urls)),  # Isso inclui todas as rotas para os ViewSets registrados
]

