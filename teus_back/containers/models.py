import sys
sys.path.append('..')
from django.db import models
from users.models import User
from info.models import City, Container, Line
from unixtimestampfield.fields import UnixTimeStampField

STATUSES = (
    ('в работе', 'в работе'),
    ('в архиве', 'в архиве'),
    ('выполнен', 'выполнен'),
    ('удален', 'удален'),
)


class UserRequest(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='amount')
    city = models.ManyToManyField(City, related_name='cities',default=1, blank=True)
    line = models.ForeignKey(Line, related_name='line', on_delete=models.CASCADE,default=1, blank=True)
    container = models.ForeignKey(Container, related_name='container', on_delete=models.CASCADE,default=1, blank=True)
    request_date = UnixTimeStampField(verbose_name='date', null=True, blank=True)
    end_date = UnixTimeStampField(verbose_name='end date', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUSES, default='в работе')

    class Meta:
        ordering = ['-end_date', '-pk']

class UserProposition(models.Model):
    user = models.ForeignKey(User, related_name='user_proposition', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='amount')
    city = models.ForeignKey(City, related_name='city_proposition', on_delete=models.CASCADE,default=1, blank=True)
    line = models.ForeignKey(Line, related_name='line_proposition', on_delete=models.CASCADE,default=1, blank=True)
    container = models.ForeignKey(Container, related_name='container_proposition', on_delete=models.CASCADE, default=1, blank=True)
    start_date = UnixTimeStampField(verbose_name='start date', null=True, blank=True)
    end_date = UnixTimeStampField(verbose_name='end date', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUSES, default='в работе')
    created_at = UnixTimeStampField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['-end_date', '-pk']
       
