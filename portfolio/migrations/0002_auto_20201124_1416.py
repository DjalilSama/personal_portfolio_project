# Generated by Django 3.1.3 on 2020-11-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='picturs/portfolio/images/'),
        ),
    ]