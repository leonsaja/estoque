from django.urls import path
from django.views.generic import TemplateView
app_name='core'
urlpatterns=[
    path('index',TemplateView.as_view(template_name='index.html'))
]