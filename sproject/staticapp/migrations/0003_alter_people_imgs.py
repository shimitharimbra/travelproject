# Generated by Django 3.2.7 on 2021-09-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0002_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='imgs',
            field=models.ImageField(upload_to='people'),
        ),
    ]
