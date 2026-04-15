from rest_framework import serializers
from .models import Cliente, Produto, Pedido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_nome(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Nome muito curto")
        return value


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'