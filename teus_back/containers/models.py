import sys
sys.path.append('..')
from django.db import models
from users.models import User
from info.models import City, Container, Line
from django.db.models import Q
from unixtimestampfield.fields import UnixTimeStampField
from teus.func import send_push
from django.db.models.signals import post_save
import logging
logger = logging.getLogger('django')

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
       

def create_proposition(sender: UserProposition, instance: UserProposition, created, **kwargs):
    if created:
        requests =  UserRequest.objects.filter(
            Q(status='в работе') &
            Q(city__name=instance.city) &
            Q(container__name__contains=instance.container.name) &
            (
                (
                    Q(request_date__gte=instance.start_date) &
                    Q(request_date__lte=instance.end_date) &
                    Q(end_date__gte= instance.end_date)
                ) |
                (
                    Q(request_date__gte=instance.start_date) &
                    Q(end_date__lte=instance.end_date)
                ) |
                (
                    Q(request_date__lte=instance.start_date) &
                    Q(end_date__lte=instance.end_date) &
                    Q(end_date__gte= instance.start_date)
                ) |
                (
                    Q(request_date__lte=instance.start_date) &
                    Q(end_date__gte= instance.end_date)
                ) 
            ) &
            Q(line__name__contains=instance.line.name) 
        )
        if requests.exists():
            for _request in requests:
                logger.warning(f"{_request.user.onesignal_token} --> player id user->{_request.user.pk}")
                if _request.user.onesignal_token != '' and _request.user.onesignal_token is not None:
                    send_push(
                            'TEUs',
                            f'''{_request.user.first_name} Появились предложения по вашему запросу''',
                            _request.user.onesignal_token,
                            {'request':_request.pk}
                        )

post_save.connect(create_proposition, sender=UserProposition)
