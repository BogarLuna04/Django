from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos


# Create your views here.
def busquedaProductos(request):
    return render(request, "busquedaProductos.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje="El articulo buscado %r"%request.GET["prd"]
        producto=request.GET["prd"]
        if len(producto) > 20:
            mensaje= "Texto de búsqueda demasiado largo"
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            return render(request,"resultadosBusqueda.html",{'Articulos':articulos,'query':producto})
    else:
        mensaje="No se ingresó nada"
    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        return render(request, "gracias.html")
    return render(request, "contacto.html")