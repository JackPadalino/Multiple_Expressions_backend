# Generated by Django 4.2.9 on 2024-01-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(choices=[('Techno', 'Techno'), ('Hardgroove', 'Hardgroove'), ('Disco', 'Disco'), ('Nu-Disco', 'Nu-Disco'), ('Funk', 'Funk'), ('House', 'House')], max_length=255, unique=True),
        ),
    ]