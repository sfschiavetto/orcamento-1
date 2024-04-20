from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import criar_pedido


urlpatterns = [
    path('all/', views.all, name="all"),
    path('login/', views.login, name="login"),
    path('base/', views.base, name="base"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('excluir_pedido/<int:pedido_id>/', views.excluir_pedido, name='excluir_pedido'),
    path('imprimir_pedido/<int:pedido_id>/', views.imprimir_pedido, name='imprimir_pedido'),
    path('criar_pedido/', criar_pedido, name='criar_pedido'),
    path('impressao/', views.imprimir_pedido, name="impressao"),
    
    
    
    
    
]
