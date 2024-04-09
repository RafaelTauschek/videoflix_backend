import datetime
from django.db import models

# Create your models here.
class Video(models.Model):
    FSK_CHOICES = [
        (0, '0'),
        (6, '6'),
        (12, '12'),
        (16, '16'),
        (18, '18')
    ]
    title = models.CharField(max_length=200, default='', blank=False)
    description = models.TextField(max_length=1000, default='', blank=False)
    file = models.FileField(null=False, blank=False)
    fsk = models.IntegerField(choices=FSK_CHOICES)
    created_at =  models.DateField(default=datetime.date.today)
    img = models.FileField(null=False, blank=False)
    genre = models.CharField(max_length=100, blank=True)
    duration_time = models.IntegerField()