from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_view, name='projects'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('descargar-cv/', views.descargar_cv, name='descargar_cv'),
    path('experience/', views.experience, name='experience'),

]