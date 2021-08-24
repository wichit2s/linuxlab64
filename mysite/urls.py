from django.contrib import admin
from django.urls import path, include
from agprice.views import index

urlpatterns = [
    #path('agprice/', include('agprice.urls')),
    path('agprice/', index),
    path('admin/', admin.site.urls),
]
