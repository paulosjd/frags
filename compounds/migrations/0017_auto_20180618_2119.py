# Generated by Django 2.0.4 on 2018-06-18 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0016_auto_20180617_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='additional_cas',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AlterField(
            model_name='compound',
            name='cid_number',
            field=models.IntegerField(blank=True, verbose_name='PubChem API CID number'),
        ),
        migrations.AlterField(
            model_name='compound',
            name='smiles',
            field=models.CharField(default='', max_length=100, verbose_name='SMILES string'),
        ),
        migrations.AlterField(
            model_name='compoundnotes',
            name='compound',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='compounds.Compound'),
        ),
        migrations.AlterField(
            model_name='compoundnotes',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='compounds.Profile'),
        ),
    ]
