# Generated by Django 4.0.2 on 2022-04-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Appointment_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='worker_id',
            field=models.IntegerField(default=0),
        ),
    ]