# Generated by Django 4.2.6 on 2023-12-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0055_booktrain_train'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPlane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('plane_name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('dest', models.CharField(max_length=30)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plane_name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('dest', models.CharField(max_length=30)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('rem', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
