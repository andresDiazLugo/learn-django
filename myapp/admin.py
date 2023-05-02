from django.contrib import admin
from .models import Project, Task
# Register your models here.
#aca vamos a colocar nuestras clases que creamos para las tablas y basciamente vamos a usar elç
#modulo admin qie mps va a permitir agregar nuestras tablas en la seccion que nos da django para administrar nuestro proyecto
admin.site.register(Project)
admin.site.register(Task)