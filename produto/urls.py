from django.urls import  path
from . import  views



app_name = 'produto'
urlpatterns = [

    path('cadastrar/produto', views.CadastrarProdutoView.as_view(), name='cadastrar_produto'),
    path('listar/produtos', views.ListProdutosView.as_view(), name='listar_produtos'),
    path('detail/produto/<int:pk>', views.DetailProdutoView.as_view(), name='detail_produto'),
    path('editar/produto/<int:pk>', views.EditarProdutoView.as_view(), name='editar_produto'),
    path('<int:pk>/json', views.produtoJson, name='produto_json'),


]

