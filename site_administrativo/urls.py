from django.urls import path
from site_administrativo.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('editar-produto/<int:id>/', editarProduto, name='editarProduto'),
    path('excluir-produto/<int:id>/', excluir_produto, name='excluir_produto'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)