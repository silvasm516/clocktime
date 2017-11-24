from django.db import models

# Create your models here.

class Drivers(models.Model):
    Email   =  models.EmailField(max_length = 20)
    FirstName = models.CharField(max_length = 20)
    



    def __str__(self):
        return self.Email





class Run(models.Model):
    Date = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 20)
    In =   models.CharField(max_length = 20, default="" )
    Out   =   models.CharField(max_length = 20, default="" )
    Duration =  models.CharField(max_length = 20, default="" )
    


    def __str__(self):
        a = self.id
        return str(a)
