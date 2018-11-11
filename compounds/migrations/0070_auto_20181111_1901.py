# Generated by Django 2.0.4 on 2018-11-11 19:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0069_auto_20181108_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enzyme',
            name='pdb_number',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('[\\w]{4}', 'String should be a valid PDB number')], verbose_name='PDB number'),
        ),
        migrations.AlterUniqueTogether(
            name='enzyme',
            unique_together={('pdb_number', 'mechanism')},
        ),
    ]
