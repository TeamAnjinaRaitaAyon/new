# Generated by Django 4.2.11 on 2024-11-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0075_healthissue_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthissue',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
