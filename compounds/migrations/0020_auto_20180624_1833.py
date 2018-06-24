# Generated by Django 2.0.4 on 2018-06-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0019_auto_20180622_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='odortype',
            name='description',
        ),
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='substructure',
            name='description',
            field=models.CharField(blank=True, default='', max_length=625),
        ),
    ]
