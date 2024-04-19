import datetime
from django.db import models
from .choices import *

class Video(models.Model):

    title = models.CharField(max_length=200, default='', blank=False)
    description = models.TextField(max_length=1000, default='', blank=False)
    video_file = models.FileField(null=True, blank=True, upload_to='videos')
    fsk = models.IntegerField(choices=FSK_CHOICES, default=0)
    created_at =  models.DateField(default=datetime.date.today)
    thumbnail = models.FileField(null=True, blank=True, upload_to='thumbnails')
    genre = models.CharField(max_length=100, blank=True)
    duration_time = models.IntegerField(blank=True, null=True, default=0)
    genre = models.CharField(choices=GENRE_CHOICES, default='', blank=True, null=True, max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, default='', blank=True, null=True, max_length=100)

    def __str__(self):
        return self.title





