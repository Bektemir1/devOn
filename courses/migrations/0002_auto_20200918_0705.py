# Generated by Django 3.1.1 on 2020-09-18 01:05

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, verbose_name='Очередной номер Раздела'),
        ),
    ]
