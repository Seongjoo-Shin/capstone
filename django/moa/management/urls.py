from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('aboutcafe/', views.aboutcafe, name='aboutcafe'),


]
