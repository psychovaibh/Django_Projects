# Generated by Django 3.2.18 on 2023-07-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='pin',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
