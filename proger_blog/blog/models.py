from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Пост/Запись"""
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='posts',
        verbose_name='Теги'
    )
    title = models.CharField("Название поста", max_length=100)
    slug = models.SlugField('Url', max_length=255, unique=True)
    content = models.TextField('Контент', blank=True)
    views = models.IntegerField('Колличество просмотров', default=0)
    image = models.ImageField("Фото", blank=True, null=True,
                              help_text='Не обязательно!')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]


class Tag(models.Model):
    """Тэг"""
    title = models.CharField('Тег', max_length=50)
    slug = models.SlugField('Url', max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Category(models.Model):
    """Категория проекта"""
    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField('Url', max_length=50, unique=True)
    description = models.CharField('Краткое описание категории', max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Project(models.Model):
    """Проект"""
    name = models.CharField('Название проекта', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    project_technology = models.CharField('Технология проекта', max_length=50)
    content = models.TextField('Контент')
    image = models.ImageField(
        'Изображение',
        blank=True,
        null=True,
        help_text='Не обязательно, система подставит стандартное изображение'
    )
    objective_of_the_project = models.CharField('Цель проекта', max_length=255)
    link_to_git = models.CharField('Ссылка на проект', max_length=255)

    def __str__(self):
        return str(self.pk) + " " + str(self.name)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-name']
