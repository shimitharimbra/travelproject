# Generated by Django 3.2.7 on 2021-09-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0003_alter_people_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='names',
            field=models.CharField(max_length=100),
        ),
    ]