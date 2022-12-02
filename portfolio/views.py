from django.shortcuts import render
#импорт модели проекта
from .models import Project

def home(request):
    #получить данные из базы данных
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html',{'projects':projects})
