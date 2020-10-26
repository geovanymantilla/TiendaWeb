from django.urls import path

from producto import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('',views.Inicio,name="Inicio"),
    path('productos/',views.Producto, name="Productos"),
    path('categoria/<int:categoria_id>/', views.Categoria, name="categoria")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)