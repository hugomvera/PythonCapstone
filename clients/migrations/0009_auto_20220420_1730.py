# Generated by Django 3.2.13 on 2022-04-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_delete_registereduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='applicationId',
            field=models.CharField(default='0', max_length=999999),
        ),
        migrations.AddField(
            model_name='client',
            name='balance',
            field=models.FloatField(default=0.0, max_length=999999),
        ),
    ]