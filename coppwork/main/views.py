import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import WorkerRegistrationForm, CompanyRegistrationForm, AddResumeForm
from django.contrib.auth import logout
from django.views.generic import UpdateView, DeleteView
from .models import Vacancy, Worker, User, Resume, Company, VacancyCategories


def index(request):
    vacancy = Vacancy.objects.all
    category = VacancyCategories.objects.all
    resume = Resume.objects.all
    context = {
        'category': category,
        'vacancy': vacancy,
        'resume': resume,
    }
    return render(request, 'main/index.html', context)


def vacancy(request):
    vacancy = Vacancy.objects.all
    context = {
        'vacancy': vacancy,
    }
    return render(request, 'main/vacancy.html', context)


def about_vacancy(request, id):
    vacancy = Vacancy.objects.get(pk=id)
    context = {
        'vacancy': vacancy,
    }
    return render(request, 'main/about-vacancy.html', context)


def about_company(request, id):
    company = Company.objects.get(pk=id)
    company_vacancy = Vacancy.objects.filter(company=id)
    context = {
        'company': company,
        'company_vacancy': company_vacancy,
    }
    return render(request, 'main/about-company.html', context)


def about_resume(request, id):
    resume = Resume.objects.get(pk=id)
    worker_resume = Resume.objects.filter(worker=resume.worker) & Resume.objects.exclude(pk=resume.id)
    res = resume.worker.age % 10
    context = {
        'resume': resume,
        'res': res,
        'worker_resume': worker_resume,
    }
    return render(request, 'main/about-resume.html', context)


def resume(request):
    resume = Resume.objects.all
    context = {
        'resume': resume,
    }
    return render(request, 'main/resume.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'error': 'Неверные учетные данные'})

    return render(request, 'main/login.html')


def reg(request):
    return render(request, 'main/reg.html')


def log(request):
    return render(request, 'main/log.html')


def add_resume(request, id):
    worker = Worker.objects.get(pk=id)
    if request.method == 'POST':
        form = AddResumeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Резюме добавлено успешно!')
            return redirect('profile', id=worker.id)
        else:
            messages.error(request, 'Неверные данные')
    else:
        form = AddResumeForm()
        context = {
            'form': form,
        }

    return render(request, 'main/add-resume.html', context)


def registration(request):
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
        else:
            messages.error(request, 'Неверные учетные данные')
    else:
        form = WorkerRegistrationForm()

    return render(request, 'main/registration.html', {'form': form})


def registration_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
        else:
            messages.error(request, 'Неверные учетные данные')
    else:
        form = CompanyRegistrationForm()

    return render(request, 'main/registration-company.html', {'form': form})


def profile(request, id):
    worker = Worker.objects.get(pk=id)
    resume = Resume.objects.filter(worker=id)
    res = worker.age % 10
    # filename = resume.file

    context = {
        'worker': worker,
        'resume': resume,
        'res': res,
        # 'filename': filename,
    }
    return render(request, 'main/profile.html', context)


class profileEditWorker(UpdateView):
    model = Worker
    template_name = 'main/profile-edit-worker.html'
    fields = ["name", "phone", "address", "gender", "age", "avatar"]


class profileEditResume(UpdateView):
    model = Resume
    template_name = 'main/profile-edit-resume.html'
    fields = ["specializations", "salary", "work_experience", "type_employment", "work_schedule", "education", "file"]


class ResumeDelete(DeleteView):
    model = Resume
    success_url = '/profile/{worker_id}'
    template_name = 'main/profile-resume-delete.html'


def profile_resume(request, id):
    resume = Resume.objects.get(pk=id)
    # filename = resume.file

    context = {
        'resume': resume,
        # 'filename': filename,
    }
    return render(request, 'main/profile-resume.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')

