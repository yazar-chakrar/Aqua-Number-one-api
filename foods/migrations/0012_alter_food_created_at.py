# Generated by Django 4.1.1 on 2022-10-01 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0011_alter_category_slug_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 1, 16, 35, 33, 106044), verbose_name='Food Created at'),
        ),
    ]
