# Generated by Django 4.2.14 on 2024-08-05 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_trip_public_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_edit', models.BooleanField(default=False)),
                ('can_comment', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invited_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_invitations', to=settings.AUTH_USER_MODEL)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='main_app.trip')),
            ],
        ),
    ]
