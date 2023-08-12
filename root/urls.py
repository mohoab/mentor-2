from django.urls import path as pt
from . import views


app_name='root'


urlpatterns = [
    pt('',views.home , name='home'),
    pt('trainers',views.trainers , name='trainers'),
    pt('about',views.about , name='about'),
    pt('contact',views.contact , name='contact'),
]

