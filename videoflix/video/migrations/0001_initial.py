# Generated by Django 5.0.4 on 2024-04-11 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='', max_length=1000)),
                ('file', models.FileField(upload_to='')),
                ('fsk', models.IntegerField(choices=[(0, '0'), (6, '6'), (12, '12'), (16, '16'), (18, '18')])),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('img', models.FileField(upload_to='')),
                ('genre', models.CharField(blank=True, max_length=100)),
                ('duration_time', models.IntegerField()),
            ],
        ),
    ]
