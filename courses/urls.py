from django.urls import path as pt
from . import views


app_name='courses'

urlpatterns = [
    pt('course', views.courses , name='courses') ,
]