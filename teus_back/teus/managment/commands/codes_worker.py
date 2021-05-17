import logging
import time
import traceback
from datetime import  datetime
from django.core.management import BaseCommand
from django.db.models import Q
from users.models import Phone
logger = logging.getLogger('django')

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while True:
            try:
                for phone in Phone.objects.filter(
                    Q(is_checked=True) |
                    Q(expires_at__gte=datetime.now())
                ):
                    logger.warning(f"{phone.phone} --> DELETED")
                    phone.delete()

            except KeyboardInterrupt:
                return
            except:
                traceback.print_exc()

            try:
                time.sleep(2)
            except KeyboardInterrupt:
                return
