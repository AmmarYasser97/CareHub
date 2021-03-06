# Generated by Django 2.1.2 on 2019-02-12 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0024_timeslots_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslots',
            name='name',
        ),
        migrations.AddField(
            model_name='timeslots',
            name='taken',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='service',
            name='timeSlots',
        ),
        migrations.AddField(
            model_name='service',
            name='timeSlots',
            field=models.ManyToManyField(default=None, to='Clinics.TimeSlots'),
        ),
    ]
