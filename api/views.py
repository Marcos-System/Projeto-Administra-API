from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProdutoListAndCreate(APIView):
    def get(self, request):                  
        produto = Produto.objects.all() 
        serializer = ProdutoSerializer(produto, many=True)
        return Response(serializer.data)