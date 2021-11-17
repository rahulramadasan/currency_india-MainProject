from django.urls import path

from currency import views

urlpatterns = [


  path('',views.home,name='home'),
  path('redirect', views.take_img, name='take_img'),
    ]