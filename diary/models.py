from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30, default='Моя заметка',
                             verbose_name='Заголовок заметки',
                             help_text='Напишите заголовок заметки')
    text = models.TextField(max_length=500,
                            verbose_name='Запись в дневнике',
                            help_text='Сделайте запись в дневник')
    is_changed = models.BooleanField(default=False,
                                     verbose_name='Показать была ли редактирована заметка')
    date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


