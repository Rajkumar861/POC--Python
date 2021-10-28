from django.db import models

# Create your models here.

class Product(models.Model):
    
    def nameFile(instance,filename):
        return '/'.join(['Images', str(instance.name), filename])


    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    images = models.ImageField(upload_to=nameFile,blank=True)
    

    def __str__(self):
        return self.name