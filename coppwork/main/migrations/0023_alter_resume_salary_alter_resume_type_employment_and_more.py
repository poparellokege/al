# Generated by Django 5.0.2 on 2024-04-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_resume_specializations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.IntegerField(verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='type_employment',
            field=models.CharField(choices=[('None', 'Не указано'), ('employment-1', 'От месяца'), ('employment-2', 'От 2х недель'), ('employment-3', 'Неделя'), ('employment-4', '3 месяца')], default='None', max_length=50, verbose_name='Тип занятости'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='work_experience',
            field=models.CharField(choices=[('None', 'Не указано'), ('work-1', 'ИНЖЕНЕРНЫЕ СЕТИ'), ('work-2', 'РЕСТАВРАЦИЯ'), ('work-3', 'СТРОИТЕЛЬСТВО ЗДАНИЙ И СООРУЖЕНИЙ'), ('work-4', 'ПРОЕКТИРОВАНИЕ ЗДАНИЙ И СООРУЖЕНИЙ'), ('work-5', 'ИНЖЕНЕРНЫЕ ИЗЫСКАНИЯ')], default='None', max_length=50, verbose_name='Время'),
        ),
    ]
