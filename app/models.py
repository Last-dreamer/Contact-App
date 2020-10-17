from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User


class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.IntegerField()
    info = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    # ordering by the new added contact
    class Meta:
        ordering = ('-id',)
