# Generated by Django 2.1 on 2018-08-20 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooler', '0006_school_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='city',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
