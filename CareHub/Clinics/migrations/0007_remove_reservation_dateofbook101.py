# Generated by Django 2.1.2 on 2019-02-08 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0006_reservation_dateofbook101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='DateOfBook101',
        ),
    ]