# Generated by Django 2.0.7 on 2018-07-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ng', '0002_auto_20180723_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userng',
            name='q_filled',
            field=models.BooleanField(default=False),
        ),
    ]
