# Generated by Django 5.0 on 2024-04-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_rename_result_examination_patientid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
    ]
