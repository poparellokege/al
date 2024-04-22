from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.urls import reverse_lazy


class User(AbstractUser):
    phone = models.CharField('Телефон', max_length=18)
    address = models.CharField('Адрес', max_length=255, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admin'


class Worker(User):
    name = models.CharField('ФИО', max_length=255)
    gender_choices = [
        ('None', 'Не указано'),
        ('Male', 'Мужчина'),
        ('Female', 'Женщина'),
    ]
    gender = models.CharField('Пол', max_length=20, choices=gender_choices, default='None')
    age = models.IntegerField('Возраст')
    avatar = models.ImageField(upload_to='images/users/workers/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return f'/profile/{self.id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Company(User):
    name = models.CharField('Название', max_length=255)
    site = models.CharField('Сайт', max_length=255, blank=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class VacancyCategories(models.Model):
    category = models.CharField('Категории работ', max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория работ'
        verbose_name_plural = 'Категории работ'


class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField('Описание', max_length=255)
    description_position = models.TextField('Краткое описание', blank=True)
    salary = models.IntegerField('Стоимость')
    category = models.ForeignKey(VacancyCategories, on_delete=models.CASCADE)
    work_experience_choices = [
        ('None', 'Не указано'),
        ('employment-1', 'От месяца'),
        ('employment-2', 'От 2х недель'),
        ('employment-3', 'Неделя'),
        ('employment-4', '3 месяца'),
    ]
    work_experience = models.CharField('Время', max_length=50, choices=work_experience_choices, default='None')
    type_employment_choices = [
        ('None', 'Не указано'),
        ('work-1', 'ИНЖЕНЕРНЫЕ СЕТИ'),
        ('work-2', 'РЕСТАВРАЦИЯ'),
        ('work-3', 'СТРОИТЕЛЬСТВО ЗДАНИЙ И СООРУЖЕНИЙ'),
        ('work-4', 'ПРОЕКТИРОВАНИЕ ЗДАНИЙ И СООРУЖЕНИЙ'),
        ('work-5', 'ИНЖЕНЕРНЫЕ ИЗЫСКАНИЯ'),
    ]
    type_employment = models.CharField('Тип работ', max_length=50, choices=type_employment_choices, default='None')
    work_schedule_choices = [
        ('None', 'Не указано'),
    ]
    work_schedule = models.CharField('-', max_length=50, choices=work_schedule_choices, default='None')
    education_choices = [
        ('None', 'Не указано'),
    ]
    education = models.CharField('-', max_length=50, choices=education_choices, default='None')
    created = models.DateField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "files/resume/worker/%Y/%m/%d/user_{0}/{1}".format(instance.worker.id, filename)


class Resume(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    specializations = models.CharField('Краткое описание',max_length=255, blank=True)
    salary = models.IntegerField('Стоимость')
    work_experience_choices = [
        ('None', 'Не указано'),
        ('work-1', 'ИНЖЕНЕРНЫЕ СЕТИ'),
        ('work-2', 'РЕСТАВРАЦИЯ'),
        ('work-3', 'СТРОИТЕЛЬСТВО ЗДАНИЙ И СООРУЖЕНИЙ'),
        ('work-4', 'ПРОЕКТИРОВАНИЕ ЗДАНИЙ И СООРУЖЕНИЙ'),
        ('work-5', 'ИНЖЕНЕРНЫЕ ИЗЫСКАНИЯ'),
    ]
    work_experience = models.CharField('Время', max_length=50, choices=work_experience_choices, default='None')
    type_employment_choices = [
        ('None', 'Не указано'),
        ('employment-1', 'От месяца'),
        ('employment-2', 'От 2х недель'),
        ('employment-3', 'Неделя'),
        ('employment-4', '3 месяца'),
    ]
    type_employment = models.CharField('-', max_length=50, choices=type_employment_choices, default='None')
    work_schedule_choices = [

    ]
    work_schedule = models.CharField('-', max_length=50, choices=work_schedule_choices, default='None')
    education_choices = [
    ]
    education = models.CharField('-', max_length=50, choices=education_choices, default='None')
    created = models.DateField('Дата добавления', auto_now_add=True)
    file = models.FileField(upload_to=user_directory_path, blank=True,  validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    def __str__(self):
        return self.specializations

    def get_absolute_url(self):
        return f'/profile-resume/{self.id}'

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'