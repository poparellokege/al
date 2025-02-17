# Generated by Django 4.2.11 on 2024-04-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_vacancycategories_vacancy_description_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='work_experience',
            field=models.CharField(choices=[('None', 'Не указано'), ('employment-1', 'Полная занятость'), ('employment-2', 'Частичная занятость'), ('employment-3', 'Стажировка'), ('employment-4', 'Оформление по ГПХ или  по совместительству')], default='None', max_length=20, verbose_name='Тип занятости'),
        ),
    ]
