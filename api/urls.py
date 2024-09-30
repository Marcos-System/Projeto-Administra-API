from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('produto/', views.ProdutoListAndCreate.as_view(), name='ProdutoListAndCreate'),

]