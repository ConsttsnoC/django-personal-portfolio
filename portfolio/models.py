from django.db import models
# создаем класс для работы с базой данный
class Project(models.Model):
    #прописываем атрибуты классов
#создаем заголовки
    title = models.CharField(max_length=100)
#создаем описание
    descriptoin = models.CharField(max_length=250)
#создаем картинки. upload_to в какой папке будут лежать картинки.
    image = models.ImageField(upload_to='portfolio/images/')
#будут кликабельны некоторые окна(картинки)/ blank=True параметр позволяющий
#открывать ссылку в новой вкладке
    url = models.URLField(blank=True)
#возвращает имя по умолчанию при новедении курсора в админ-панели
    def __str__(self):
        return self.title