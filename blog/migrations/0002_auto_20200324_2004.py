# Generated by Django 2.2 on 2020-03-24 14:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 3, 24, 14, 34, 19, 847990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='level',
            field=models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('expert', 'expert')], max_length=10),
        ),
    ]
