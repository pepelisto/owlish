from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import CustomersList, customer_detail
import random

class Tests(TestCase):

    def test_customers_list_view_status_code(self):
        urls = ['customers_list']
        for u in urls:
            url = reverse(u)
            response = self.client.get(url)
            self.assertEquals(response.status_code, 200)

    def test_url_resolves_views(self):
        r = random.randint(1, 999)
        list = [['/customers_list/', CustomersList.as_view()],
                ['/customer_detail/' + str(r) + '/', customer_detail]]
        for i in list:
            view = resolve(i[0]).func
            self.assertEquals(view.__name__, i[1].__name__)
            self.assertEquals(view.__module__, i[1].__module__)
