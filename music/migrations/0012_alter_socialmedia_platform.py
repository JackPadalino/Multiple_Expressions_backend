# Generated by Django 5.0.1 on 2024-02-13 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_alter_socialmedia_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='platform',
            field=models.CharField(choices=[('instagram', 'instagram'), ('soundcloud', 'soundcloud'), ('mixcloud', 'mixcloud'), ('tiktok', 'tiktok'), ('twitch', 'twitch'), ('facebook', 'facebook'), ('twitter', 'twitter')], max_length=255),
        ),
    ]
