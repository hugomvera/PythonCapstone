# Generated by Django 3.2.13 on 2022-04-19 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_registereduser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegisteredUser',
        ),
    ]