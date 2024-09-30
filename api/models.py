from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False)
    tipo = models.CharField(max_length=50, null=False)
    descricao = models.TextField(null=False)
    valor = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    imagem = models.ImageField(null=False,upload_to ='produtos/')