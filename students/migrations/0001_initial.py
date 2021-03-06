# Generated by Django 3.1.1 on 2020-09-18 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='courses.course', verbose_name='Название курса')),
                ('course_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_owner', to=settings.AUTH_USER_MODEL, verbose_name='Владелец курса')),
            ],
            options={
                'verbose_name': 'Студент курса',
                'verbose_name_plural': 'Студенты курсов',
                'ordering': ['-created'],
            },
        ),
    ]
