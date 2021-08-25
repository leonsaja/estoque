from django.urls import path
from django.views.generic import TemplateView
app_name='estoque'
urlpatterns = [
    path('',TemplateView.as_view(template_name='estoque/index.html'),name='estoque_index'),

]