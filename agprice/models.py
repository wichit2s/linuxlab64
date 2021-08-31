from django.db import models

# Create your models here.
class Price(models.Model):
    id           = models.AutoField(primary_key=True, verbose_name='รหัส')
    image        = models.ImageField(upload_to='price/', verbose_name='ภาพประกอบ')
    date         = models.DateTimeField(auto_now=True, verbose_name='วันที่ประกาศ')
    product_name = models.CharField(max_length=300, default='', verbose_name='สินค้า')
    market_name  = models.CharField(max_length=300, default='', verbose_name='ตลาด')
    price        = models.FloatField(default=0.0, verbose_name='ราคา')

    def __str__(self):
        return f'{self.product_name} ราคา {self.price} บาท'
