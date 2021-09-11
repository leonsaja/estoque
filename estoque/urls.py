from django.urls import path
from django.views.generic import TemplateView
from estoque.views import  estoque_views
from estoque.views import estoque_itens_views
app_name='estoque'

urlpatterns = [
    path('',TemplateView.as_view(template_name='estoque/index.html'),name='estoque_index'),
    path('entrada/',estoque_views.EstoqueEntradaListView.as_view(), name='estoque_entrada_list'),
    path('saida/',estoque_views.EstoqueSaidaListView.as_view(), name='estoque_saida_list'),
    path('detalhe/entrada/<int:pk>/', estoque_views.EstoqueEntradadeteilView.as_view(), name='estoque_entrada_detail'),
    path('detalhe/saida/<int:pk>/', estoque_views.EstoqueSaidadeteilView.as_view(), name='estoque_saida_detail'),
    #Estoque Item
    path('entrada/estoque/', estoque_itens_views.add_entrada_estoque, name='add_entrada_estoque'),
    path('saida/estoque/', estoque_itens_views.dar_saida_estoque, name='dar_saida_estoque'),


]