# Generated by Django 3.0.4 on 2020-04-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200411_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='photo2',
        ),
        migrations.AlterField(
            model_name='menu',
            name='photo',
            field=models.CharField(default='menu/images/breakfast/idly.jpg', max_length=100),
            preserve_default=False,
        ),
    ]
