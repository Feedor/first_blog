from django.conf import settings
from django.db import models
from django.utils import timezone
class Post(models.Model):
    #models.ForeignKey - ссылка на другую модель 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models.CharField —  текстовое поле с ограничением на количество символов.
    title = models.CharField(max_length=200)
    #models.TextField - поле для неограничено длинного текста
    text = models.TextField()
    #models.DateTimeField- дата и время
    create_date = models.DateTimeField(default=timezone.now)
    pulikate_date = models.DateTimeField(blank=True, null=True)
    def publ(self):
        self.pulikate_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
