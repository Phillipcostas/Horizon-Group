# Generated by Django 4.2.14 on 2024-08-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suitcaseitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]