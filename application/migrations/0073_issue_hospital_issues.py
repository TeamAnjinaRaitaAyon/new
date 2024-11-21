# Generated by Django 4.2.11 on 2024-11-21 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0072_delete_appointment_delete_book_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='issues',
            field=models.ManyToManyField(blank=True, to='application.issue'),
        ),
    ]