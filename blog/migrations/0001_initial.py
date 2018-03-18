# Generated by Django 2.0.3 on 2018-03-18 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('time', models.DateTimeField(blank=True, verbose_name=datetime.datetime.now)),
            ],
        ),
    ]
