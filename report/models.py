from django.conf import settings
from django.db import models



class Members(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    surf_experiece = models.CharField(max_length=30)
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.name

class Locations(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    beach_name = models.CharField(max_length=60)
    ocean = models.CharField(max_length=60)
    nearest_airport = models.CharField(max_length=60)
    shark_activity = models.CharField(max_length=60)
    anual_shark_attacks = models.IntegerField(default=0)
    required_experience = models.CharField(max_length=60)


    def __str__(self):
        return self.beach_name

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    price = models.CharField(max_length=60)
    used = models.CharField(max_length=60)
    warranty = models.CharField(max_length=60)
    images = models.FileField(upload_to='report/static/images')
    date_posted = models.DateTimeField()

    def get_image(self):
        if self.images and hasattr(self.images, 'url'):
            return self.images.url
        else:
            return False

    def __str__(self):
        return self.item