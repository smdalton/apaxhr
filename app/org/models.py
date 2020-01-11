from django.db import models

# geographic data organization:

class Region(models.Model):
    choices = (('N', 'APAX North'),('S', 'APAX South'))
    description = models.CharField(choices=choices, max_length=50, blank=False, null=False)

class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

# generic working location
class WorkLocation(models.Model):
    choices = (('lc','Learning Center'),('aw','Administrative Workplace'),('ot','other'))
    type = models.CharField(choices=choices, max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

class Department(models.Model):
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
