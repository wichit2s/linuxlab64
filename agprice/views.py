from django.shortcuts import render
from .models import Price

# Create your views here.
def index(req):
    prices = Price.objects.all()
    return render(req, 'agprice/index.html', { 'prices': prices })

def about(req):
    return render(req, 'agprice/about.html')
