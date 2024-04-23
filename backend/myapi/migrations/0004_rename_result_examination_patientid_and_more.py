# Generated by Django 5.0.1 on 2024-04-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_point_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examination',
            old_name='result',
            new_name='patientID',
        ),
        migrations.RenameField(
            model_name='pointresult',
            old_name='examination',
            new_name='examinationID',
        ),
        migrations.RenameField(
            model_name='pointresult',
            old_name='point',
            new_name='pointID',
        ),
        migrations.AlterField(
            model_name='examination',
            name='exID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pointresult',
            name='resID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
