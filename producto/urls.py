from django.urls import path

from producto import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('productos/',views.productos, name="Productos"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)