# Generated by Django 4.2.5 on 2023-10-11 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0033_countryministries_ministerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministerprimarydetails',
            name='MinisterID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='application.politiciansprimarydetails'),
        ),
        migrations.AlterField(
            model_name='ministerprimarydetails',
            name='MinistryName',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='application.countryministries'),
        ),
        migrations.AlterField(
            model_name='mpelection',
            name='Candidate1ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Candidate1ID', to='application.usersprimarydetails'),
        ),
        migrations.AlterField(
            model_name='mpelection',
            name='Candidate2ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Candidate2ID', to='application.usersprimarydetails'),
        ),
        migrations.AlterField(
            model_name='politiciansprimarydetails',
            name='PoliticianID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='application.usersprimarydetails'),
        ),
    ]
