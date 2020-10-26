from django.shortcuts import render

from producto.models import producto , empresa , categoria , marca

# Create your views here.
def Inicio(request):
    productos = producto.objects.all()
    empresas = empresa.objects.all()
    return render(request, "producto/index.html", {"empresas" : empresas , "productos" : productos})

# def empresas(request):
#     empresas = empresa.objects.all()
#     return render(request, "producto/base.html", {"empresas" : empresas})    

def Producto(request):
    productos = producto.objects.all()
    empresas = empresa.objects.all()
    categorias = categoria.objects.all()
    marcas = marca.objects.all()
    return render(request, "producto/productos.html", {"productos" : productos , "empresas" : empresas , "categorias" : categorias , "marcas" : marcas})

def Categoria(request, categoria_id):
    categorias=categoria.objects.get(id=categoria_id)
    productos= producto.objects.filter(categoria=categorias)
    marcas = marca.objects.all()
    empresas = empresa.objects.all()
    listadoCategoria= categoria.objects.all()
    return render (request, "producto/categoria.html", {"listadoCategoria": listadoCategoria, "categorias" : categorias , "productos": productos ,"empresas" : empresas , "marcas": marcas})

    

