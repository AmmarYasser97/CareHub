# Generated by Django 2.1.2 on 2019-02-07 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0008_auto_20190207_2311'),
        ('reservations', '0002_auto_20190207_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Doctor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Staff.Doctor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Clinic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Clinics.Service'),
        ),
    ]
