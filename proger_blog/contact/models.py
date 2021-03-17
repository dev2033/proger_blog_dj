from django.db import models


class Contact(models.Model):
    """Подписка по email"""
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    email = models.EmailField('Email', max_length=50)
    message = models.TextField('Сообщение')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
