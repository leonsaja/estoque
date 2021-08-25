from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import  CreateView,ListView
from produto.forms import CadastrarProdutoForm
from produto.models import Produto


class CadastrarProdutoView(CreateView):

    form_class =CadastrarProdutoForm
    template_name = 'produto/form_produto.html'

class ListProdutosView(ListView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'produto/produto_list.html'



