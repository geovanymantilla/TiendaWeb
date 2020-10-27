from django.shortcuts import render

from producto.models import producto , empresa , categoria , marca

# Create your views here.
def Inicio(request):
    productos = producto.objects.all()
    empresas = empresa.objects.all()
    return render(request, "producto/index.html", {"empresas" : empresas , "productos" : productos})

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

def Marca(request, marca_id):
    marcas = marca.objects.get(id=marca_id)
    productos = producto.objects.filter(marca=marcas)
    categorias = categoria.objects.all()
    empresas = empresa.objects.all()
    listadoMarca= marca.objects.all()
    return render (request, "producto/marca.html", {"listadoMarca": listadoMarca, "categorias" : categorias , "productos": productos,"empresas" : empresas , "marcas": marcas})

def DetalleProducto(request, idCurso):
    productos = producto.objects.get(idCurso=idCurso)
    empresas = empresa.objects.all()
    categorias = categoria.objects.all()
    marcas = marca.objects.all()
    return render(request, "producto/detalle.html", {"empresas": empresas, "productos": productos, "marcas": marcas, "categorias" : categorias} )