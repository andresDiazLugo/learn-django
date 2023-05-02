from django.shortcuts import render
from django.http import HttpResponse,JsonResponse#jsonResponse nos va a permitir devolver multiples elementos
from .models import Project, Task
from django.shortcuts import get_object_or_404,render,redirect#render nos permite devolver archivos html en el navegador en ves de enviar string en formato html
from .forms import CreateNewTask
from .forms import CreateNewProject
# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request,"index.html",{
        'title':title
    })
def about(request):
    username = 'andres'
    return render(request,"about.html",{
        'username':username
    })
def hello(request,username):
    print(username)
    return HttpResponse(f"<h1>Hello {username}</h1>")
def id(request,id):
    # print(id)
    return HttpResponse("este es el id %s"%id)
def project(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    # print(projects)
    return render(request, "project.html",{
        'projects':projects
    })
def tasks(request):

    # task = get_object_or_404(Task,id=id)#esta funcion nos permite devolver un 404 not found cuando surja un error en la busqueda de un registro en la base de datos
    tasks = Task.objects.all()
    print("this task",tasks)
    return render(request,"task.html",{
        'tasks':tasks
    })
def create_task(request):

    if request.method == 'GET':
       
        return render(request, 'create_task.html',{
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=1)
        return redirect('tasks')
def create_project(request):
  if request.method == 'GET':
        return render(request, 'create_project.html',{
        'form': CreateNewProject()
    })
  else:
        print("este es el post@@@",request.POST)
        Project.objects.create(name=request.POST["name"])
        print(project)
        return redirect('projects')
def project_detail(request, id):
    print(id)
    # project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id = id)
    tasks = Task.objects.filter(project_id = id)
    return render(request, 'detail.html',{
        'project': project,
        'tasks': tasks
    })