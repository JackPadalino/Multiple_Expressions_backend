# Generated by Django 5.0.1 on 2024-03-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0019_alter_track_track_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
