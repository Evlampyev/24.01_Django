# Generated by Django 5.0.1 on 2024-01-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfirst', '0005_alter_judge_competitions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='competitions',
            field=models.ManyToManyField(blank=True, default='Нет', to='appfirst.competition'),
        ),
    ]
