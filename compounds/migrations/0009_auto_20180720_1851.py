# Generated by Django 2.0.4 on 2018-07-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0008_bioactive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bioactive',
            name='trade_name',
        ),
        migrations.AddField(
            model_name='bioactive',
            name='chemical_name',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Chemical name'),
        ),
    ]
