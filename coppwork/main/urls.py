from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import user_login, user_logout

urlpatterns = [
    path('', views.index, name='home'),
    path('vacancy', views.vacancy, name='vacancy'),
    path('resume', views.resume, name='resume'),
    path('about-vacancy/<int:id>', views.about_vacancy, name='about-vacancy'),
        path('about-company/<int:id>', views.about_company, name='about-company'),
    path('about-resume/<int:id>', views.about_resume, name='about-resume'),
    path('login', user_login, name='login'),
    path('reg', views.reg, name='reg'),
    path('log', views.log, name='log'),
    path('add-resume/<int:id>', views.add_resume, name='add-resume'),
    path('registration', views.registration, name='registration'),
    path('registration-company', views.registration_company, name='registration-company'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('profile/<int:pk>/profile-edit-worker', views.profileEditWorker.as_view(), name='profile-edit-worker'),
    path('profile-resume/<int:id>', views.profile_resume, name='profile-resume'),
    path('profile-resume/<int:pk>/profile-edit-resume', views.profileEditResume.as_view(), name='profile-edit-resume'),
    path('profile-resume/<int:pk>/profile-resume-delete', views.ResumeDelete.as_view(), name='profile-resume-delete'),
    path('logout', user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)