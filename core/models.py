from django.db import models
from django.core.exceptions import ValidationError


# Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


# Produto
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome


# Pedido
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.quantidade * self.produto.preco

    def save(self, *args, **kwargs):
        # valida estoque
        if self.quantidade > self.produto.quantidade:
            raise ValidationError("Quantidade maior que o estoque disponível")

        # diminui estoque
        self.produto.quantidade -= self.quantidade
        self.produto.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"