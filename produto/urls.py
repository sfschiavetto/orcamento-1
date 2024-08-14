from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('produto_cadastrado/', views.produto_cadastrado, name='produto_cadastrado'),
]
