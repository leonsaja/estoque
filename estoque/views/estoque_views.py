
from estoque.models import Estoque
from django.views.generic import ListView, DetailView, CreateView


class EstoqueEntradaList(ListView):
      model = Estoque
      template_name = 'estoque/estoque_entrada_list.html'
      queryset = Estoque.objects.filter(movimento='E')
      context_object_name = 'objs'

class EstoqueEntradadeteil(DetailView):
      model = Estoque
      template_name = 'estoque/estoque_detail.html'

      def get_context_data(self, **kwargs):
            context=super(EstoqueEntradadeteil, self).get_context_data(**kwargs)
            context['obj']=Estoque.objects.get(pk=self.kwargs['pk'])

            return context
      
class EstoqueSaidaList(ListView):
      model = Estoque
      template_name = 'estoque/estoque_saida_list.html'
      queryset = Estoque.objects.filter(movimento='S')
      context_object_name = 'objs'


class EstoqueSaidadeteil(DetailView):
      model = Estoque
      template_name = 'estoque/estoque_detail.html'

      def get_context_data(self, **kwargs):
            context = super(EstoqueSaidadeteil, self).get_context_data(**kwargs)
            context['obj'] = Estoque.objects.get(pk=self.kwargs['pk'])
            return context




