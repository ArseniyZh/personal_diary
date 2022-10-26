# Generated by Django 4.1.2 on 2022-10-24 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_remove_profile_diary'),
        ('diary', '0006_remove_post_owner_post_diary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='diary',
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Diary',
        ),
    ]