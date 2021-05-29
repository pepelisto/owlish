import csv
from django.conf import settings
import django
import googlemaps
import os
from owlish.settings import DATABASES, INSTALLED_APPS, SECRET_KEY, BASE_DIR
settings.configure(
    DATABASES=DATABASES,
    INSTALLED_APPS=INSTALLED_APPS,
    SECRET_KEY=SECRET_KEY,
)
django.setup()
from challenge.models import *

Customer.objects.all().delete()
City.objects.all().delete()
Title.objects.all().delete()
Company.objects.all().delete()
