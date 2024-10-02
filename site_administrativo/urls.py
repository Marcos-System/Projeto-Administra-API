from django.urls import path
from site_administrativo.views import *
from django.conf.urls.static import static
from django.conf import settings
app_name = 'site_administrativo'

urlpatterns = [
    path('', home, name='home'),
    path('editar-produto/<int:id>/', editarProduto, name='editarProduto'),
    path('excluir-produto/<int:id>/', excluir_produto, name='excluir_produto'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)