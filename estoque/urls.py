from django.urls import path
from django.views.generic import TemplateView
from .views import EstoqueEntradaListView
app_name='estoque'

urlpatterns = [
    path('',TemplateView.as_view(template_name='estoque/index.html'),name='estoque_index'),
    path('movimento/entrada/', EstoqueEntradaListView.as_view(), name='entrada_estoque'),

]