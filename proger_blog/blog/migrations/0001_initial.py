# Generated by Django 3.1.7 on 2021-03-14 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ('description', models.CharField(max_length=255, verbose_name='Краткое описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тег')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('project_technology', models.CharField(max_length=50, verbose_name='Технология проекта')),
                ('content', models.TextField(verbose_name='Контент')),
                ('image', models.ImageField(blank=True, help_text='Не обязательно, система подставит стандартное изображение', null=True, upload_to='', verbose_name='Изображение')),
                ('objective_of_the_project', models.CharField(max_length=255, verbose_name='Цель проекта')),
                ('link_to_git', models.CharField(max_length=255, verbose_name='Ссылка на проект')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название поста')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('views', models.IntegerField(default=0, verbose_name='Колличество просмотров')),
                ('image', models.ImageField(blank=True, help_text='Не обязательно!', null=True, upload_to='', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-created_at'],
            },
        ),
    ]
