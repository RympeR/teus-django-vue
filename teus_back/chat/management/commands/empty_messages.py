import logging
import traceback
from django.core.management import BaseCommand
from chat.models import *
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.utils import timezone
from teus.func import send_push
import time
logger = logging.getLogger('django')

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while True:
            try:
                qs = Chat.objects.filter(
                        (Q(text='') | Q(text__isnull=True) )& Q(attachment__in=['', None])
                )
                logger.warning(f'deleted {len(qs)} empty messages')
                qs.delete()
            except KeyboardInterrupt:
                return
            except:
                traceback.print_exc()

            try:
                time.sleep(3600)
            except KeyboardInterrupt:
                return
