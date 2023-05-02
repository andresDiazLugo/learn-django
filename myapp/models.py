from django.db import models

# Create your models here.
class Project(models.Model):#esta clase project va a eredar los modelos que me da django
    name = models.CharField(max_length=200) #agrego los atributos que voy a estar guardando en la tabla charField es como decirle va a ser un texto

    def __str__(self):#con esta funcion vamos a poder devolver un string en ves de un objecto cuando se instance la clase
        return self.name#te permite mostrar el nombre de projecto en la seccion de administracion de django
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):#con esta funcion vamos a poder devolver un string en ves de un objecto cuando se instance la clase
        return self.title+'-'+self.project.name
    #relacionamos una tabla, un ejemplo que pasa si elimino un projecto que pasa con 
    #esa tarea que le pertenece un proyecto es por eso que usamos la opcion on_delete 
    #de esta forma se elimina los datos de las dos relaciones si elimino un projecto tambien se eliminara la tarea que le pertenece a ese projecto