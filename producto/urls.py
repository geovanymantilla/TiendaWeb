from django.urls import path

from producto import views

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('productos/',views.productos, name="Productos"),
]