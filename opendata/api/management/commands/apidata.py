import json
import os
import sys

from django.core.management.base import BaseCommand
from api import models
from . import _data

class Command(BaseCommand):
    
    help = 'Add records to database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--action',
            required=False,
            choices=["load", "display", "delete"],
            dest='action',
            help='Specify action',
        )

    def handle(self, *args, **options):
        action = options['action']

        if str(action) == "load":
            self.load()
        
        if str(action) == "display":
            self.display()

        if str(action) == "delete":
            self.delete()


    def load(self):
        self.stdout.write('Loading data to database...')
        #self.load_provinces()
        self.load_universities()
        #self.load_faculties()
        self.stdout.write('Loading data to database...done.')

    
    def load_universities(self):
        self.stdout.write('Loading universities data to database...')
        universities = _data.get_universities()

        for university in universities:
            current_university = models.University(
                short_name = university["id"],
                long_name = university["name"],
                address = university["address"],
                phone = university["phone"],
                email = university["email"],
                url = university["url"],
                status = university["type"]
            )
            current_university.save()

            for city in university["cities"]:
                try:
                    current_city = models.City.objects.get(name=str(city).upper())
                    current_university.cities.add(current_city)
                except models.City.DoesNotExist:
                    print ("City isn't in the database yet.")
                else:

                    print ("City %s is in the database." %(city))

        self.stdout.write('Loading universities data to database...done.')


    def load_faculties(self):
        self.stdout.write('Loading faculties data to database...')
        self.stdout.write('Loading faculties data to database...done.')


    def load_provinces(self):
        self.stdout.write('Loading province data to database...')
        provinces = _data.get_provinces()
        for province in provinces:
            self.load_province(province)
        self.stdout.write('Loading province data to database...done.')


    def load_province(self, province):
        current_province = models.Province(name=province["lib_dep"])
        current_province.save()
        for commune in province["communes"]:
            city = models.City(name=commune["lib_com"])
            city.save()
            for arrondissement in commune["arrondissements"]:
                district = models.District(name=arrondissement['lib_arrond'])
                district.save()
                for quartier in arrondissement["quartiers"]:
                    neighborhood = models.Neighborhood(name=quartier['lib_quart'])
                    neighborhood.save()
                    district.neighborhoods.add(neighborhood)
                city.districts.add(district)
            current_province.cities.add(city)            

    
    def display(self):
        self.stdout.write("Total universities %s" %(len(models.University.objects.all())))
        self.stdout.write("Total provinces %s" %(len(models.Province.objects.all())))
       

    def delete(self):
        pass
