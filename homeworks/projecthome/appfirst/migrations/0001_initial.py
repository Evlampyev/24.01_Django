# Generated by Django 5.0.1 on 2024-01-16 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fullname', models.CharField(default=None, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appfirst.competition')),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Имя')),
                ('patronymic', models.CharField(default=None, max_length=25, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('post', models.CharField(max_length=100, verbose_name='Занимаемая должность')),
                ('regalia', models.TextField(default=None, verbose_name='Заслуги и регалии')),
                ('organization', models.CharField(max_length=100, verbose_name='Место работы')),
                ('status', models.CharField(choices=[('M', 'главный судья'), ('J', 'судья'), ('S', 'секретарь'), ('O', 'наблюдатель')], default='O', max_length=1, verbose_name='Статус на соревнованиях')),
                ('competition', models.ManyToManyField(to='appfirst.competition')),
            ],
            options={
                'db_table': 'judges',
            },
        ),
    ]
