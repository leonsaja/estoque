from django.urls import  path
from . import  views

app_name = 'produto'
urlpatterns = [

    path('cadastar/produto', views.CadastrarProdutoView.as_view(), name='cadastrar_produto'),
    path('listar/produtos', views.ListProdutosView.as_view(), name='listar_produtos'),
]