import sys
sys.path.append('..')
from django.db import models
from users.models import User
from info.models import City, Container, Line

class UserRequest(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='amount')
    city = models.ForeignKey(City, related_name='city', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, related_name='line', on_delete=models.CASCADE)
    container = models.ForeignKey(Container, related_name='container', on_delete=models.CASCADE)
    request_date = models.DateField(verbose_name='date')

class UserProposition(models.Model):
    user = models.ForeignKey(User, related_name='user_proposition', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='amount')
    city = models.ForeignKey(City, related_name='city_proposition', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, related_name='line_proposition', on_delete=models.CASCADE)
    container = models.ForeignKey(Container, related_name='container_proposition', on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date')

class Deal(models.Model):
    user_request = models.ForeignKey(User, related_name='deal_user_request', on_delete=models.CASCADE)
    user_proposition = models.ForeignKey(User, related_name='deal_user_proposition', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Кол-во')
    city = models.ForeignKey(City, related_name='city_deal', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, related_name='line_deal', on_delete=models.CASCADE)
    container = models.ForeignKey(Container, related_name='container_deal', on_delete=models.CASCADE)
    handshake_time = models.DateTimeField(auto_now_add=True)
