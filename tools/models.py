from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class Tool(models.Model):

    TYPES = [
        ('Automobile', 'Auto'),
        ('Plumbing', 'Plumbing'),
        ('Bike', 'Bike'),
        ('Yard', 'Yard'),
        ('Woodworking', 'Woodworking'),
    ]
    BOOL = [
    (True, 'Yes'),
    (False, 'No')
]   

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tool = models.CharField(max_length = 50, default = '')
    type = models.CharField(max_length = 30, choices=TYPES, default='AUTO')
    posted = models.DateField(default=datetime.date.today)
    available = models.BooleanField(choices=BOOL)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.tool

    def get_absolute_url(self):
        return reverse('tools:index')