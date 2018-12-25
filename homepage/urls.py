from django.conf.urls import url 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^about/',views.about, name='about'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^home/', views.home, name='register'),
]