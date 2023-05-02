from django.urls import path
from . import views#del directorio actual importame todo el archivo views
urlpatterns =  [
    path('', views.index, name="index"),#mostrame en la ruta principal lo que ejecute la funcion hello
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello,  name="hello"),
    path('search/<int:id>', views.id, name="search"),
    path('projects/', views.project, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/',views.create_project, name="create_project")
]