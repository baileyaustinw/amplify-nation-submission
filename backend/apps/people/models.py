from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    car_make = models.CharField(max_length=200)

    def __unicode__(self):
    	return self.name