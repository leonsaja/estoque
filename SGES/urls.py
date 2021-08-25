from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estoque/',include('estoque.urls', namespace='estoques')),
    path('produto/',include('produto.urls', namespace='produto')),
    path('', include('core.urls', namespace='core')),

]
