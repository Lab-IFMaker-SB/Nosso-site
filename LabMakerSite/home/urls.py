from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='bem-vindos'),
    path('about/', views.about, name='quem-somos'),
    path('projects/', views.projects, name='projetos'),
    path('activities/', views.activities, name='atividades'),
    path('courses/', views.courses, name='cursos'),
    path('contact/', views.contact, name='contato')
]
