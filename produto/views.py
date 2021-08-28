from django.views.generic import CreateView, ListView, DetailView
from produto.forms import CadastrarProdutoForm
from produto.models import Produto
from django.db.models import Q
class CadastrarProdutoView(CreateView):
    form_class =CadastrarProdutoForm
    template_name = 'produto/form_produto.html'

class ListProdutosView(ListView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'produto/produto_list.html'


    def get_queryset(self):
        queryset=super(ListProdutosView, self).get_queryset()
        search=self.request.GET.get('search')
        if search:
            queryset=queryset.filter(Q(produto__icontains=search)| Q(ncm__icontains=search))

        return queryset

class DetailProdutoView(DetailView):
    model = Produto
    template_name = 'produto/produto_detail.html'
    context_object_name = 'produto'

    #
    # def get_context_data(self, **kwargs):
    #     context=super(DetailProdutoView, self).get_context_data(**kwargs)
    #     context['produto']=Produto.objects.get(pk=self.kwargs['pk'])
    #
    #     return context