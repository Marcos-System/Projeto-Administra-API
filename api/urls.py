from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('produto/', views.ProdutoList.as_view(), name='ProdutoListAndCreate'),
    path('produto/<int:id>/', views.ProdutoDetail.as_view(), name='produto-detail'), 
]