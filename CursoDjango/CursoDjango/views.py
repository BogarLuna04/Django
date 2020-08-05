from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template #sirve para cargar templates (plantillas)
from django.shortcuts import render
class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def primeraVista(request):

    P1=Persona("Bogar","Luna")
    doc_externo = open("/Users/bogarluna/GitHub/Django/CursoDjango/CursoDjango/plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    fecha=datetime.datetime.now()
    ejemplo="Esto es parte del ejemplo de variables"
    temasCurso =["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    ctx=Context({"nombre":P1.nombre,"apellido":P1.apellido,"ejemplo1":ejemplo,"fecha":fecha,"temas":temasCurso})
    documento=plt.render(ctx)
    return HttpResponse(documento)



def segundaVista(request): 
    #Manejo de templates con get_template
    P1=Persona("Bogar","Luna")
    fecha=datetime.datetime.now()
    ejemplo="Esto es parte del ejemplo de variables"
    temasCurso =["Plantillas","Modelos","Formularios","Vistas","Despliegue"]


    #doc_externo=get_template('plantilla1.html')
    #documento=doc_externo.render(({"nombre":P1.nombre,"apellido":P1.apellido,"ejemplo1":ejemplo,"fecha":fecha,"temas":temasCurso}))
    #return HttpResponse(documento)
    return render(request,'plantilla1.html',{"nombre":P1.nombre,"apellido":P1.apellido,"ejemplo1":ejemplo,"fecha":fecha,"temas":temasCurso})

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


def comidas(request):
    fecha=datetime.datetime.now()
    return render(request,"comidas.html",{"fecha":fecha})

def desayunos(request):
    fecha=datetime.datetime.now()
    return render(request,"desayunos.html",{"fecha":fecha})