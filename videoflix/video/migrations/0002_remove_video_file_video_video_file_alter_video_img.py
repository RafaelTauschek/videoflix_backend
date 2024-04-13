# Generated by Django 5.0.4 on 2024-04-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='file',
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]