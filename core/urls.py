from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/novo/', views.criar_produto, name='criar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/novo/', views.criar_pedido, name='criar_pedido'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/novo/', views.criar_cliente, name='criar_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),
]