from django.contrib import admin
from django.urls import path, include
#from agprice.views import index, about
from myapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('agprice/', include('agprice.urls')),
    #path('', index),
    #path('about/', about),
    path('', views.index),
    path('about/', views.about),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
