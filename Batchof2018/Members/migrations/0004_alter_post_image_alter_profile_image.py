# Generated by Django 5.1.1 on 2024-09-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='Profilepic/'),
        ),
    ]
