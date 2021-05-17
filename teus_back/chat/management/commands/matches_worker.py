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
                        logger.warning(f"{_filter.user.onesignal_token} --> player id")
                        if _filter.user.onesignal_token != '' and _filter.user.onesignal_token is not None:
                            send_push(
                                    'TEUs',
                                    f'''{_filter.user.first_name} Появились предложения по вашему запросу''',
                                    _filter.user.onesignal_token,
                                    {'request':_filter.pk}
                                )
                            break
                for request_ in UserRequest.objects.all():
                    if datetime.now().timestamp() > request_.end_date.timestamp():
                        request_.status = 'в архиве'
                        request_.save()
                for proposition in UserProposition.objects.all():
                    if datetime.now().timestamp() > proposition.end_date.timestamp():
                        proposition.status = 'в архиве'
                        proposition.save()
            except KeyboardInterrupt:
                return
            except:
                traceback.print_exc()

            try:
                time.sleep(3600)
            except KeyboardInterrupt:
                return
