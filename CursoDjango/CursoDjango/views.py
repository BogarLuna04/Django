from django.http import HttpResponse
import datetime

def primeraVista(request):
    return HttpResponse("Estoy en la primer vista" )

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