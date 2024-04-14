# Generated by Django 5.0.4 on 2024-04-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_alter_video_fsk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='img',
        ),
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='thumbnails'),
        ),
    ]