# Generated by Django 3.1.7 on 2021-03-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210326_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file_project',
        ),
        migrations.AddField(
            model_name='project',
            name='file_project',
            field=models.FileField(blank=True, help_text='Не обязательно', null=True, upload_to='', verbose_name='Загрузка файлов проекта'),
        ),
    ]