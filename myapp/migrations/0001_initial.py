# Generated by Django 3.2.6 on 2021-09-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=1000)),
                ('county', models.CharField(blank=True, default='', max_length=200)),
                ('lat', models.FloatField(blank=True, default=0.0)),
                ('lng', models.FloatField(blank=True, default=0.0)),
                ('image', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]