from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ProdutoList(APIView):
    def get(self, request):
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many=True)
        return Response(serializer.data)



class ProdutoDetail(APIView):
    def get(self, request, id):
        produto = get_object_or_404(Produto, id=id)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
