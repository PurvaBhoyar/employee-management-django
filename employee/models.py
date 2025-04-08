# employee/models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)

    ROLE_CHOICES = [
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('Manager', 'Manager'),
        ('Tester', 'Tester'),
        ('HR', 'HR'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Developer')

    def __str__(self):
        return self.name
