from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('perimetry/', views.perimetry, name='perimetry'),
    path('get_points/', views.get_points, name='get_points'),
    path('emailing/', views.emailing, name='emailing'),
    path('examination/', views.examination, name='examination'),
    path('get_perimetry_pdf/', views.get_perimetry_pdf, name='get_perimetry_pdf'),
    path('get_ishihara_pdf/', views.get_ishihara_pdf, name='get_ishihara_pdf'),
    path('get_examination_type/', views.get_examination_type, name='get_examination_type'),
    path('registry/', views.registry, name='registry'),
    path('get_patient_info/', views.get_patient_info, name='get_patient_info'),
    path('get_examinations/', views.get_examinations, name='get_examinations'),
    path('ishihara/', views.ishihara, name='ishihara'),
    path('create_dummy_patient/', views.create_dummy_patient, name='create_dummy_patient'),
    path('delete_patient_data/', views.delete_patient_data, name='delete_patient_data')
]