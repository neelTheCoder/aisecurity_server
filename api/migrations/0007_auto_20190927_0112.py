# Generated by Django 2.2.5 on 2019-09-27 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_studentdateinoutstatus_resolved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdateinoutstatus',
            old_name='status',
            new_name='in_school',
        ),
    ]