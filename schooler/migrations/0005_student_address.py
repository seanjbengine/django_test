# Generated by Django 2.1 on 2018-08-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooler', '0004_auto_20180817_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
