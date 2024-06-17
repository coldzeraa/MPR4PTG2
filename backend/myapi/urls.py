from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('perimetry/', views.perimetry, name='perimetry'),
    path('get_points/', views.get_points, name='get_points'),
    path('examination/', views.examination, name='examination')
]