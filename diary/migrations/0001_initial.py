# Generated by Django 4.1.2 on 2022-10-26 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Моя заметка', help_text='Напишите заголовок заметки', max_length=30, verbose_name='Заголовок заметки')),
                ('text', models.TextField(help_text='Сделайте запись в дневник', max_length=500, verbose_name='Запись в дневнике')),
                ('is_changed', models.BooleanField(default=False, verbose_name='Показать была ли редактирована заметка')),
                ('date', models.DateTimeField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
