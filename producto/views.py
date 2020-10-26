from django.shortcuts import render

from producto.models import producto , empresa

# Create your views here.
def inicio(request):
    productos = producto.objects.all()
    empresas = empresa.objects.all()
    return render(request, "producto/index.html", {"empresas" : empresas , "productos" : productos})

# def empresas(request):
#     empresas = empresa.objects.all()
#     return render(request, "producto/base.html", {"empresas" : empresas})    

def productos(request):
    productos = producto.objects.all()
    empresas = empresa.objects.all()
    return render(request, "producto/productos.html", {"productos" : productos , "empresas" : empresas})

