from django.urls import path

from . import views

app_name = 'form_sample'
urlpatterns = [
    path('', views.MyFormView.as_view(), name='index'),
]
