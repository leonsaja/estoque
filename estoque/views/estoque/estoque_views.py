
from estoque.models import Estoque
from django.views.generic import ListView, DetailView, CreateView


class EstoqueEntradaListView(ListView):
      model = Estoque
      template_name = 'estoque/estoque_entrada_list.html'
      queryset = Estoque.objects.filter(movimento='E')
      context_object_name = 'objs'



class EstoqueEntradadeteilView(DetailView):
      model = Estoque
      template_name = 'estoque/estoque_entrada_detail.html'

      def get_context_data(self, **kwargs):
            context=super(EstoqueEntradadeteilView, self).get_context_data(**kwargs)
            context['obj']=Estoque.objects.get(pk=self.kwargs['pk'])

            return context




