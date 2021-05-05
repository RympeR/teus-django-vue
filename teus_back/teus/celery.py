from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teus.settings')

_celery = Celery(
    'config',
    backend='redis://localhost',
    broker='pyamqp://',
    include=['containers.tasks', 'chat.tasks']
)


_celery.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    _celery.start()
