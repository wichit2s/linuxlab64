from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from agprice.models import Price
import codecs, json

class Command(BaseCommand):
    help = 'load json ไฟล์ จาก https://data.go.th/dataset/34'
    MONTHS = { 
            'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 
            'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12 
            }

    def add_arguments(self, parser):
        parser.add_argument('name')

    def save_pricee(d):
        p = Price()
        a = d['PRICE_DATE'].split('-')
        dd,mm,yy = int(a[0]),MONTHS[a[1]],int(a[2])+2000
        p.date = timezone.datetime(year=yy, month=mm, day=dd)
        p.product_name = d['PR_PROD_NAME']
        p.market_name = d['MARKET_NAME']
        p.price = d['PRICE_DAY']
        p.save()
        return p

        
    def handle(self, *args, **options):
        #print(args)
        #print('-------------')
        #print(options)
        fname = options['name']
        data = json.load(codecs.open(fname, 'r', 'utf-8-sig'))
        for d in data:
            print(self.save_price(d))

