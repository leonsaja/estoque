from django.urls import path
from django.views.generic import TemplateView
from estoque.views.estoque import  estoque_views
from estoque.views.estoque_itens import estoque_itens_views
app_name='estoque'

urlpatterns = [
    path('',TemplateView.as_view(template_name='estoque/index.html'),name='estoque_index'),
    path('movimento/entrada/',estoque_views.EstoqueEntradaListView.as_view(), name='estoque_entrada_list'),
    path('detalhe/entrada/<int:pk>/', estoque_views.EstoqueEntradadeteilView.as_view(), name='estoque_entrada_detail'),


    #Estoque Item
    path('add/entrada/', estoque_itens_views.AddEntradaEstoqueView.as_view(), name='add_entrada_estoque'),


]