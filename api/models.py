from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Produto(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Usuário"), on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, null=False)
    tipo = models.CharField(max_length=50, null=False)
    descricao = models.TextField(null=False)
    valor = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    imagem = models.ImageField(null=False,upload_to ='produtos/')