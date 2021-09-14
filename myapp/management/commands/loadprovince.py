from django.core.management.base import BaseCommand, CommandError
from myapp.models import Province

class Command(BaseCommand):
    help = 'load province from "https://wichit2s.gitlab.io/python/_static/data/Thailand-Provinces.json"'

    def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        import requests
        url = 'https://wichit2s.gitlab.io/python/_static/data/Thailand-Provinces.json'
        provinces = requests.get(url).json()
        print(type(provinces))
        print(provinces[0])
        for p in provinces:
            a = Province(
                        name   = p['PROVINCE'],
                        county = p['COUNTY'],
                        lat    = p['LATITUDE'],
                        lng    = p['LONGITUDE'],
                        image  = p['IMAGE']
                    )
            a.save()
