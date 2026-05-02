from django.db import models
from simple_history.models import HistoricalRecords

class Student(models.Model):

    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)   
    roll_number = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100)


    extra_data = models.JSONField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_progress'
    )

    
    joined_date = models.DateField(auto_now_add=True)

    
    is_active = models.BooleanField(default=True)

    
    profile_url = models.URLField(null=True, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

