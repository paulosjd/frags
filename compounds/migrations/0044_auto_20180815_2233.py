# Generated by Django 2.0.4 on 2018-08-15 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0043_auto_20180813_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='compoundsource',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.CompoundSource'),
        ),
        migrations.AlterField(
            model_name='compoundsource',
            name='amount',
            field=models.FloatField(max_length=10),
        ),
    ]