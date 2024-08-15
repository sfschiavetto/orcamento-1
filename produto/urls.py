from django.urls import path
from produto import views

urlpatterns = [
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('produto_cadastrado/', views.produto_cadastrado, name='produto_cadastrado'),
    path('deletar_produto/<str:id>/', views.deletar_produto, name="deletar_produto"),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
]
