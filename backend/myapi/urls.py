from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('perimetry/', views.perimetry, name='perimetry'),
    path('get_points/', views.get_points, name='get_points'),
    path('emailing/', views.emailing, name='emailing'),
    path('examination/', views.examination, name='examination'),
    path('get_pdf/', views.get_pdf, name='get_pdf'),
    path('registry/', views.registry, name='registry'),
    path('get_patient_info/', views.get_patient_info, name='get_patient_info'),
    path('get_examinations/', views.get_examinations, name='get_examinations')
]