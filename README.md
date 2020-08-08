# Django
Iniciar la creación de un sitio 

$ django-admin startproject mysite

correr el sitio

$ python3 manage.py runserver
para configurar desde donde cargar los templates (plantillas) se hace desde settings


Crear tablas en la base de datos
$ python3 manage.py migrate

Crear una nueva aplicación 
$ python3 manage.py startapp gestionPedidos

Se debe declarar en aplicaciones instaladas de settings
verificar que todo se hizo correctamente 
$ python3 manage.py check gestionPedidos

realizar migracion de las tablas
$ python3 manage.py makemigrations

Crear instrucciones para crear tablas 
$ python3 manage.py sqlmigrate gestionPedidos 0001

Crear tablas en la base de datos
$ python3 manage.py migrate

Entrar al shell para realizar operaciones directas en la DB con código SQL
$ python3 manage.py shell
$ from gestionPedidos.models import Articulos  
insert
$ art=Articulos(nombre='Camisa',seccion='Confeccion',precio=100)  ----> operacion Insert
$ art.save()   ----> Se termina de guardar 
$ art2=Articulos(nombre='Carne',seccion='Alimento',precio=10) 
$ art2.save() 
$ art3=Articulos.objects.create(nombre='Tiburon',seccion='Pescado',precio=40) ---> con create
$ art4=Articulos.objects.create(nombre='platano',seccion='fruta',precio=5)
$ art5=Articulos.objects.create(nombre='vaso',seccion='utencilio',precio=50)
update
$ art.precio = 95
$ art.save() 

delete
$ art5=Articulos.objects.get(id=3)
$ art5.delete()

select
$ lista=Articulos.objects.all()

con where
$ Articulos.objects.filter(seccion='pescado')
where y and
$ Articulos.objects.filter(nombre='vaso',seccion='utencilio') 
where y >=
$ Articulos.objects.filter(precio__gte=45)
gt ---- >
where y >=
$ Articulos.objects.filter(precio__lte=45)
where y between
$ Articulos.objects.filter(precio__range=(25,70))
Order by
$ Articulos.objects.filter(precio__range=(5,70)).order_by('precio')
Order by   desc
$ Articulos.objects.filter(precio__range=(5,70)).order_by('-precio')


Ver las operaciones realizadas de python a SQL
$ lista.query.__str__() 

Constraseña Postgres 25Dediciembre

Usar Postgres como manjedor de base de datos
Se necesita instalar psycopg2
$ pip3 install psycopg2
o 
$ pip3 install psycopg2-binary ---> si falla el primero

realizar cambios de configuración de Database en settings y correr 
$ python3 manage.py makemigrations


//////
Para conectar con Oracle 
install cx_Oracle
https://gist.github.com/thom-nic/6011715 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',
        'USER': 'usuario',
        'PASSWORD': 'usuario',
        'HOST': '127.0.0.1',
        'PORT': '1521',
    }
}

SE DEBEN REALIZAR MIGRACIONES CADA QUE SE REALIZA UN CAMBIO
$ python3 manage.py makemigrations
$ python3 manage.py migrate