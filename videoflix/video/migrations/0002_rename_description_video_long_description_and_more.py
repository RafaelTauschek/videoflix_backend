# Generated by Django 5.0.4 on 2024-04-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='description',
            new_name='long_description',
        ),
        migrations.AddField(
            model_name='video',
            name='short_description',
            field=models.TextField(default='', max_length=200),
        ),
    ]