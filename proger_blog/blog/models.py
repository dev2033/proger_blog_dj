from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Пост"""
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


class Category(models.Model):
    """Виды категорий"""
    name = models.CharField(
        'Название категории для главной страницы',
        max_length=100
    )
    content = models.CharField(
        'Контент',
        max_length=150,
        help_text='Краткое описание про категорию'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
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


class Project(models.Model):
    """Проекты"""
    name = models.CharField(
        'Название проекта',
        max_length=100,
        blank=True,
        null=True,
    )
    content = models.TextField('Контент')
    image = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return str(self.pk) + " " + str(self.name)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-name']
