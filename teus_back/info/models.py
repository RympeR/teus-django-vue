from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'



class Container(models.Model):
    name = models.CharField('Название', max_length=255)
    image = models.ImageField(verbose_name='Фото контейнера')

    class Meta:
        verbose_name = 'Контейнер'
        verbose_name_plural = 'Контейнера'
        ordering = ['id']

    def __str__(self):
        return self.name


class Line(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Линия'
        verbose_name_plural = 'Линии'

