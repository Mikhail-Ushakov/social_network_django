# Generated by Django 4.1 on 2023-08-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(default='image_added/default.jpg', upload_to='image_added/'),
        ),
    ]