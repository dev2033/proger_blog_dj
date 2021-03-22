from django.db import models


class Contact(models.Model):
    """Подписка по emai"""
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    email = models.EmailField('Email', max_length=100)
    message = models.TextField('Текст сообщения')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



