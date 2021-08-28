from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estoque/',include('estoque.urls', namespace='estoques')),
    path('produto/',include('produto.urls', namespace='produto')),
    path('', include('core.urls', namespace='core')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

