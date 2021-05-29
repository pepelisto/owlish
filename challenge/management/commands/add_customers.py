import csv
from django.core.management.base import BaseCommand
import googlemaps
from owlish.settings import BASE_DIR, API_KEY
from challenge.models import *


class Command(BaseCommand):

    help = 'Create in database all users from a given list' \
           ' that havent been created before'

    def handle(self, *args, **options):
        """
        looks for the file in the project directory
        """
        with open(str(BASE_DIR) + '\customers.csv', newline='') as file:
            customers = csv.reader(file, delimiter=',', quotechar='"')
            next(customers, None)
            self.loop_trough_customers(customers=customers)

    def loop_trough_customers(self, customers):
        for row in customers:
            self.Create(
                id=row[0], first_name=row[1], last_name=row[2], email=row[3],
                gender=row[4], company=row[5], city=row[6], title=row[7],
            ).create_customer()

    class Create:

        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def create_customer(self):
            """
            Trigers the creation of all the objects related to a given customer
            """
            s = self.kwargs.get
            self.get_or_create_model_object(Title, title_name=s("title"))
            self.get_or_create_model_object(Company, company_name=s("company"))
            self.get_or_create_model_object(City, city=s("city"))
            self.get_or_create_model_object(
                Customer, id=s("id"), first_name=s("first_name"),
                last_name=s("last_name"), email=s("email"), gender=s("gender"),
                company_id=self.company_id, city_id=self.city_id,
                title_id=self.title_id
            )

        def get_or_create_model_object(self, model, **kwargs):
            """
            Check if the given object related to the customer exist and if
            it doesnt than its created, also returns de ids of the objects
            related to the custome (ex: title, city, etc)
            """
            model = model
            object, object_created = model.objects.get_or_create(**kwargs)
            if object_created:
                if model == City:
                    self.get_latitude_and_longitude(city=object.city)
                    object.longitude = self.lng
                    object.latitude = self.lat
                object.save()
                if model == Customer:
                    print('Customer succesfully created')
            else:
                if model == Customer:
                    print('Customer was already created created')
            if model == City:
                self.city_id = object.pk
            elif model == Title:
                self.title_id = object.pk
            elif model == Company:
                self.company_id = object.pk

        def get_latitude_and_longitude(self, city):
            """
            Look for coordinates in google maps API for a given "city,
            state" string, if its not found set them None
            """
            api_key = API_KEY
            try:
                gmaps_client = googlemaps.Client(api_key)
                geocode_result = gmaps_client.geocode(city)
                result = geocode_result[0]
                self.lat = result['geometry']['location']['lat']
                self.lng = result['geometry']['location']['lng']
            except:
                pass
                self.lat = None
                self.lng = None

