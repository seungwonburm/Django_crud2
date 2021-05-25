from django.db import models

# Create your models here.
class Owners(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.IntegerField()
    class Meta:
        db_table='owner'

class Dogs(models.Model):
    name=models.CharField(max_length=45)
    age=models.IntegerField()
    owner= models.ForeignKey(Owners,on_delete=models.CASCADE)
    class Meta:
        db_table='dog'