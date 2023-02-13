from django.db import models

# Create your models here.
class Students(models.Model):
    studentNumber = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    gpa = models.FloatField()
    
    def __str__(self):
        
        return f"Students: {self.first_name} {self.last_name}"
