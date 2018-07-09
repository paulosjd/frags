# Generated by Django 2.0.4 on 2018-07-09 20:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0029_compound_chemical_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compound',
            name='cas_number',
            field=models.CharField(db_index=True, max_length=20, unique=True, validators=[django.core.validators.RegexValidator('\\d+(?:-\\d+)+', 'String should be a valid CAS number')], verbose_name='CAS number'),
        ),
        migrations.AlterField(
            model_name='compound',
            name='iupac_name',
            field=models.CharField(blank=True, db_index=True, default='', editable=False, max_length=200, verbose_name='IUPAC name'),
        ),
        migrations.AlterField(
            model_name='compound',
            name='smiles',
            field=models.CharField(blank=True, db_index=True, default='', max_length=100, verbose_name='SMILES string'),
        ),
        migrations.AlterField(
            model_name='substructure',
            name='iupac_name',
            field=models.CharField(blank=True, db_index=True, default='', editable=False, max_length=200, verbose_name='IUPAC name'),
        ),
        migrations.AlterField(
            model_name='substructure',
            name='smiles',
            field=models.CharField(blank=True, db_index=True, default='', max_length=100, verbose_name='SMILES string'),
        ),
    ]
