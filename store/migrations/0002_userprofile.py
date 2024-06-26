# Generated by Django 5.0.3 on 2024-03-24 07:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state_region', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
