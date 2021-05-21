import logging
import time
import traceback
from datetime import timedelta, datetime
from django.core.management import BaseCommand
from containers.models import *
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.utils import timezone
from teus.func import send_push
import logging
logger = logging.getLogger('django')

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while True:
            try:
                for _filter in UserRequest.objects.all():
                    logger.warning(f"{_filter} -> user request fro user -> {_filter.user.pk}")
                    propositons = UserProposition.objects.filter(
                        Q(status='в работе') &
                        Q(city__name__in=_filter.city.all().values('name')) &
                        Q(container__name__contains=_filter.container.name) &
                        (
                            (
                                Q(start_date__gte=_filter.request_date) &
                                Q(start_date__lte=_filter.end_date) &
                                Q(end_date__gte= _filter.end_date)
                            ) |
                            (
                                Q(start_date__gte=_filter.request_date) &
                                Q(end_date__lte=_filter.end_date)
                            ) |
                            (
                                Q(start_date__lte=_filter.request_date) &
                                Q(end_date__lte=_filter.end_date) &
                                Q(end_date__gte= _filter.request_date)
                            ) |
                            (
                                Q(start_date__lte=_filter.request_date) &
                                Q(end_date__gte= _filter.end_date)
                            ) 
                        ) &
                        Q(line__name__contains=_filter.line.name) 
                    )
                    logger.warning(propositons)
                    if propositons.exists():
                        logger.warning(f"{_filter.user.onesignal_token} --> player id user->{_filter.user.pk}")
                        if _filter.user.onesignal_token != '' and _filter.user.onesignal_token is not None:
                            send_push(
                                    'TEUs',
                                    f'''{_filter.user.first_name} Появились предложения по вашему запросу''',
                                    _filter.user.onesignal_token,
                                    {'request':_filter.pk}
                                )
                            break
            except KeyboardInterrupt:
                return
            except:
                traceback.print_exc()

            try:
                time.sleep(180)
            except KeyboardInterrupt:
                return
