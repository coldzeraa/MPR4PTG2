from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('login/', views.login, name='login'),
    path('get_points/', views.getPoints, name='get_points')
]