# Generated by Django 4.2.14 on 2024-07-31 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_trip_end_date_alter_trip_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]