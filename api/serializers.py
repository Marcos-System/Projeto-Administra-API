from rest_framework import serializers
from api.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Produto
        fields = ['nome', 'descricao','tipo', 'valor', 'imagem']
        