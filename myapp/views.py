from django.shortcuts import render
from myapp.models import Province 

def index(req):
    provinces = Province.objects.all()
    chiangrai = provinces[0]
    return render(req, 'myapp/index.html', { 
        'provinces': provinces,
        'chiangrai': chiangrai
        } )

def about(req):
    return render(req, 'myapp/about.html')
