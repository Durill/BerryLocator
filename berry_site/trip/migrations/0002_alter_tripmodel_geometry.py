# Generated by Django 4.2.7 on 2024-02-22 18:47

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripmodel',
            name='geometry',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326),
        ),
    ]
