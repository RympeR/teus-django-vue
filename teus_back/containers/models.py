from django.db import models
import sys
sys.path.append('..')
from users.models import User
from info.models import City, Container, Line

class UserRequest(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    amount = models.IntegerField(verbose_name='amount')
    city = models.ForeignKey(City, related_name='city', on_delete=models.DO_NOTHING)
    line = models.ForeignKey(Line, related_name='line', on_delete=models.DO_NOTHING)
    container = models.ForeignKey(Container, related_name='container', on_delete=models.DO_NOTHING)
    request_date = models.DateField(verbose_name='date')


class UserProposition(models.Model):
    user = models.ForeignKey(User, related_name='user_proposition', on_delete=models.DO_NOTHING)
    amount = models.IntegerField(verbose_name='amount')
    city = models.ForeignKey(City, related_name='city_proposition', on_delete=models.DO_NOTHING)
    line = models.ForeignKey(Line, related_name='line_proposition', on_delete=models.DO_NOTHING)
    container = models.ForeignKey(Container, related_name='container_proposition', on_delete=models.DO_NOTHING)
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date')
