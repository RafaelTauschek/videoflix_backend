import os
from django.dispatch import receiver
import django_rq
from django.db.models.signals import post_save, post_delete
from django_rq import enqueue
from videoflix.video.models import Video
from video.tasks import convert_360p, convert_720p, convert_1080p

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    if created:
        print('New video created')
        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(convert_360p, instance.video_file.path)
        queue.enqueue(convert_720p, instance.video_file.path)
        queue.enqueue(convert_1080p, instance.video_file.path)
    
    
@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)