from django.db import models

# Create your models here.
class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, default='', blank=True)
    county = models.CharField(max_length=200, default='', blank=True)
    lat = models.FloatField(default=0.0, blank=True)
    lng = models.FloatField(default=0.0, blank=True)
    image = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return f'จังหวัด{self.name} ภาค{self.county} พิกัด {self.lat},{self.lng}'
