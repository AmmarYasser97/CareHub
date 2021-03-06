# Generated by Django 2.1.2 on 2019-02-12 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0014_reservation_slots'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='Slots',
        ),
        migrations.AddField(
            model_name='reservation',
            name='timeSlots',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Clinics.TimeSlots'),
        ),
        migrations.AddField(
            model_name='service',
            name='timeSlots',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Clinics.TimeSlots'),
        ),
    ]
