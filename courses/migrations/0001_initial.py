# Generated by Django 3.1.1 on 2020-09-18 00:38

import courses.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название курса')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('overview', models.TextField(verbose_name='Описание курса')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('status', models.BooleanField(default=False, verbose_name='Доступен ли курс')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('order', courses.fields.OrderField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courses.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('order', courses.fields.OrderField(blank=True)),
                ('content_description', models.TextField()),
                ('video_content', models.FileField(upload_to='videos', verbose_name='Видеоурок')),
                ('file_content', models.FileField(upload_to='files', verbose_name='Файлы для урока')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='courses.module')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
