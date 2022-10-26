from django.db import models
from django.contrib.auth.models import User
from diary import models as dm

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True,
                                  verbose_name='Имя пользователя',
                                  help_text='Введите имя пользователя')
    last_name = models.CharField(max_length=100, null=True,
                                  verbose_name='Фамилия пользователя',
                                  help_text='Введите фамилию пользователя')
    bio = models.TextField(max_length=500, null=True, blank=True,
                           verbose_name='Биография пользователя',
                           help_text='Расскажите немного о себе')


    def __str__(self):
        return self.user.first_name
