# Generated by Django 4.1.7 on 2023-03-12 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Красткое содержание')),
                ('content', models.TextField(verbose_name='Полное содеражание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2023, 3, 12, 14, 44, 47, 428589), verbose_name='Опубликована')),
            ],
            options={
                'verbose_name': 'статья блога',
                'verbose_name_plural': 'статья блога',
                'db_table': 'Posts',
                'ordering': ['-posted'],
            },
        ),
    ]
