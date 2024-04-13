import os
from django.dispatch import receiver
import django_rq
from django.db.models.signals import post_save, post_delete, pre_save
from .models import Video
from video.tasks import convert_360p, convert_720p, convert_1080p

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    if created:
        print('New video created')
        try:
            queue = django_rq.get_queue('default', autocommit=True)
            queue.enqueue(convert_360p, instance.video_file.path)
            queue.enqueue(convert_720p, instance.video_file.path)
            queue.enqueue(convert_1080p, instance.video_file.path)
        except Exception as e:
            print(f'Error enqueueing convert: {e}')
    
    
def delete_converted_files(video_path):
    base_path, extension = os.path.splitext(video_path)
    for resolution in ['_360p', '_720p', '_1080p']:
        converted_file_path = base_path + resolution + 'mp4'
        if os.path.isfile(converted_file_path):
            os.remove(converted_file_path)


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)
            delete_converted_files(instance.video_file.path)
    

@receiver(pre_save, sender=Video)
def get_video_duration(sender, instance, **kwargs):
    pass



