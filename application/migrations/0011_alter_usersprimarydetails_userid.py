# Generated by Django 4.2.5 on 2023-10-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_remove_usersprimarydetails_foreignkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprimarydetails',
            name='UserID',
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
    ]