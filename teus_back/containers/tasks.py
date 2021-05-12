from datetime import timedelta
from teus.celery import _celery
from celery.schedules import crontab
from celery.decorators import periodic_task
from containers.models import *
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.utils import timezone
from teus.func import send_push

@periodic_task(
    run_every=(crontab(minute='01', hour='01', day_of_week='*', day_of_month='*', month_of_year='*')),
    name="check_matches",
    ignore_result=True
)
def check_matches():
    for _filter in UserRequest.objects.all():
        
        propositons = UserProposition.objects.filter(
            Q(status='в работе') &
            Q(city__name__in=_filter.city.all().values('name')) &
            Q(container__name__contains=_filter.container.name) &
            (
                Q(start_date__range=(_filter.request_date, _filter.end_date)) |
                Q(end_date__range=(_filter.request_date, _filter.end_date))
            ) &
            Q(line__name__contains=_filter.line.name) & 
            Q(created_at__gte=timezone.now()-timedelta(days=1))
        )
        if propositons.exists():
            send_push(
                    'TEUs',
                    f'''{_filter.user.first_name} Появились предложения по вашему запросу''',
                    _filter.user.onesignal_token
                )