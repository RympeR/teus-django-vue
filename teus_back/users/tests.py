
from django.test import TestCase

from django.test import Client
c = Client()
response = c.post(path='/api/containers/create-deal/',
                  data={
                      'user_request': 1,
                      'amount': '44',
                      'city': 1,
                      'line': 1,
                      'container': 1,
                      'user_proposition': 2},
                  content_type='application/json')