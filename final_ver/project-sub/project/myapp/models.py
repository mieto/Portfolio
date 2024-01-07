from django.db import models

# Create your models here.
class Information(models.Model):
    date = models.DateField()
    time_slot_a = models.CharField(max_length=1) 
    time_slot_b = models.CharField(max_length=1)
    time_slot_c = models.CharField(max_length=1)
    time_slot_d = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.date}"

class Help(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    detail = models.CharField(max_length=1000)
    