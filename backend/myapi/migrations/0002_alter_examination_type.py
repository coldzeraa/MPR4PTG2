# Generated by Django 5.0 on 2024-11-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='type',
            field=models.CharField(choices=[('P', 'Perimetry'), ('I', 'Ishihara')], max_length=1),
        ),
    ]
