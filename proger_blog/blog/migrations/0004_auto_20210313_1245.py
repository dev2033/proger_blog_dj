# Generated by Django 3.1.7 on 2021-03-13 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_project_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link_to_git',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Ссылка на проект'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='objective_of_the_project',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Цель проекта'),
            preserve_default=False,
        ),
    ]
