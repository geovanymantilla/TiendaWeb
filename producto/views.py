from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "producto/index.html")

def productos(request):
    return render(request, "producto/productos.html")
