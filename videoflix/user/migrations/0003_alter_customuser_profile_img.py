# Generated by Django 5.0.4 on 2024-04-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_img',
            field=models.CharField(blank=True, default='./src/assets/profile/cat_profilepicture.jpg', max_length=150),
        ),
    ]
