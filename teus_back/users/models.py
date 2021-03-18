from django.db import models
from django.db.models import Q
import hmac
import hashlib
from dateutil.relativedelta import relativedelta
import datetime
# Create your models here.


class User(models.Model):
    phone = models.CharField(verbose_name='Телефон',
                             max_length=20, unique=True, db_index=True)
    first_name = models.CharField('Имя', max_length=255, null=True, blank=True)
    last_name = models.CharField(
        'Фамилия', max_length=255, null=True, blank=True)
    company = models.CharField(
        'Компания', max_length=255, null=True, blank=True)
    image = models.ImageField(
        verbose_name='Фото профиля', null=True, blank=True)
    push_on = models.BooleanField(default=False)
    token = models.CharField(max_length=255, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    @staticmethod
    def generate_token(msg):
        return hmac.new(bytes('qwegqwIOOLSegwGEGfef', encoding='utf8'), bytes(msg, encoding='utf8'), hashlib.sha256).hexdigest()

class Phone(models.Model):
    phone = models.BigIntegerField(db_index=True)
    code = models.IntegerField('Code', db_index=True)
    is_checked = models.BooleanField('Is checked', default=False)
    created_at = models.DateTimeField('Created at', auto_now=True)
    expires_at = models.DateTimeField('Expires at', default=datetime.date.today() + relativedelta(minutes=20))

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
