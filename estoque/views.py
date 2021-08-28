
from .models import Estoque
from django.views.generic import  ListView




class EstoqueEntradaListView(ListView):
      model = Estoque
      template_name = 'estoque/estoque_entrada_list.html'
      queryset = Estoque.objects.filter(movimento='E')
      context_object_name = 'movimentos'

