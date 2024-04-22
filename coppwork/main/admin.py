from django.contrib import admin
from .models import User, Worker, Company, Vacancy, VacancyCategories, Resume

admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(VacancyCategories)
admin.site.register(Resume)