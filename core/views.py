from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, Pedido
from .forms import ProdutoForm, PedidoForm

@login_required
def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


@login_required
def criar_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('produtos')

    return render(request, 'form_produto.html', {'form': form})


@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produtos')

    return render(request, 'form_produto.html', {'form': form})


@login_required
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produtos')
@login_required
def home(request):
    return render(request, 'home.html')

from .models import Pedido

@login_required
def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})

@login_required
def criar_pedido(request):
    form = PedidoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('pedidos')

    return render(request, 'form_pedido.html', {'form': form})

from .models import Cliente
from .forms import ClienteForm

@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


@login_required
def criar_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('clientes')

    return render(request, 'form_cliente.html', {'form': form})


@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('clientes')

    return render(request, 'form_cliente.html', {'form': form})


@login_required
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('clientes')