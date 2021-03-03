from django.db import models
from django.db.models import Q
# Create your models here.


class User(models.Model):
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    first_name = models.CharField('Имя', max_length=255, null=True, blank=True)
    last_name = models.CharField(
        'Фамилия', max_length=255, null=True, blank=True)
    company = models.CharField(
        'Компания', max_length=255, null=True, blank=True)
    image = models.ImageField(verbose_name='Фото профиля', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
