from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)   
    roll_number = models.CharField(null=True, blank=True)
    course = models.CharField(max_length=100)
    extra_data = models.JSONField(null=True, blank=True)
       


    

    def __str__(self):
        return self.name
    



