from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import Produto, Pedido, Cliente
from .forms import ProdutoForm, PedidoForm, ClienteForm

from rest_framework import viewsets
from .serializers import ClienteSerializer, ProdutoSerializer, PedidoSerializer


#  HOME 
@login_required
def home(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_produtos': Produto.objects.count(),
        'total_pedidos': Pedido.objects.count(),
    }
    return render(request, 'home.html', context)


# PRODUTOS 
@login_required
def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


@login_required
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto criado com sucesso!")
            return redirect('produtos')
        else:
            messages.error(request, "Erro ao criar produto.")
    else:
        form = ProdutoForm()

    return render(request, 'form_produto.html', {'form': form})


@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect('produtos')
        else:
            messages.error(request, "Erro ao atualizar produto.")
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'form_produto.html', {'form': form})


@login_required
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    messages.success(request, "Produto deletado com sucesso!")
    return redirect('produtos')


#  PEDIDOS 
@login_required
def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})


@login_required
def criar_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Pedido criado com sucesso!")
                return redirect('pedidos')
            except ValidationError as e:
                messages.error(request, e.message)

        else:
            messages.error(request, "Erro ao criar pedido.")
    else:
        form = PedidoForm()

    return render(request, 'form_pedido.html', {'form': form})


#  CLIENTES 
@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


@login_required
def criar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente criado com sucesso!")
            return redirect('clientes')
        else:
            messages.error(request, "Erro ao criar cliente.")
    else:
        form = ClienteForm()

    return render(request, 'form_cliente.html', {'form': form})


@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente atualizado com sucesso!")
            return redirect('clientes')
        else:
            messages.error(request, "Erro ao atualizar cliente.")
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'form_cliente.html', {'form': form})


@login_required
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, "Cliente deletado com sucesso!")
    return redirect('clientes')


#  API 
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer