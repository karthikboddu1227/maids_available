from django.db import models

class Maid(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    availability_start = models.TimeField()
    availability_end = models.TimeField()
    society=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    service=models.CharField(max_length=100)
    housesize=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    