from django.contrib import admin
# эта страница отображения в админ-панели
# импортируем класс из модел
from .models import Project
#регистрация модели которые хотим видеть в админ-панели
admin.site.register(Project)