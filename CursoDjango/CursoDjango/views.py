from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def primeraVista(request):
    P1=Persona("Alejandro","Flores")
    doc_externo = open("/Users/bogarluna/GitHub/Django/CursoDjango/CursoDjango/plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    fecha=datetime.datetime.now()
    ejemplo="Esto es parte del ejemplo de variables"
    ctx=Context({"nombre":P1.nombre,"apellido":P1.apellido,"ejemplo1":ejemplo,"fecha":fecha})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def segundaVista(request): 
    return HttpResponse("Estoy en la segunda vista" )

def fecha(request):
    fecha=datetime.datetime.now()
    documento= """
    <html> 
    <body>
    <h1>Esta es la fecha actual '%s' </h1>
    </body>
    </html>
    """%fecha
    return HttpResponse(documento)

def calculoEdad(request,edad, year):
    edadActual=edad
    periodo = year - 2020
    edadFutura = edadActual + periodo
    documento= """
    <html> 
    <body>
    <h1>En el año %s tu edad será %s años </h1>
    </body>
    </html>
    """%(year,edadFutura)
    return HttpResponse(documento)