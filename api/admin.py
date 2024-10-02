from django.contrib import admin
from .models import *

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','tipo', 'descricao', 'valor')
    list_filter = ('nome','tipo')

admin.site.register(Produto, ProdutoAdmin)