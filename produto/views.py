from django.views.generic import CreateView, ListView, DetailView,UpdateView
from produto.forms import ProdutoForm
from produto.models import Produto
from django.db.models import Q

class CadastrarProdutoView(CreateView):
    form_class =ProdutoForm
    template_name = 'produto/form_produto.html'

class ListProdutosView(ListView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'produto/produto_list.html'

    def get_queryset(self):
        queryset=super(ListProdutosView, self).get_queryset()
        search=self.request.GET.get('search')
        if search:
            queryset=queryset.filter(Q(produto__icontains=search)| \
                                     Q(ncm__icontains=search))
        return queryset

class DetailProdutoView(DetailView):
    model = Produto
    template_name = 'produto/produto_detail.html'
    context_object_name = 'produto'

class EditarProdutoView(UpdateView):
    model = Produto
    form_class =ProdutoForm
    template_name = 'produto/form_produto.html'