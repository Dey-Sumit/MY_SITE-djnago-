# Generated by Django 2.2 on 2020-03-24 05:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=40, unique=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.CharField(max_length=20)),
                ('level', models.CharField(choices=[('beg', 'beginner'), ('inter', 'intermediate'), ('expert', 'expert')], max_length=10)),
                ('language', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(verbose_name=datetime.datetime(2020, 3, 24, 5, 9, 55, 46127, tzinfo=utc))),
            ],
        ),
    ]
