import datetime
from django.db import models

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
    video_file = models.FileField(null=True, blank=True, upload_to='videos')
    fsk = models.IntegerField(choices=FSK_CHOICES, default=0)
    created_at =  models.DateField(default=datetime.date.today)
    thumbnail = models.FileField(null=True, blank=True, upload_to='thumbnails')
    genre = models.CharField(max_length=100, blank=True)
    duration_time = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.title





