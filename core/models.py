from django.db import models

# Create your models here.
class Student(models .Model):
    title = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return self.title