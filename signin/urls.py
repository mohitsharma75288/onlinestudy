from django.conf.urls import url, include
from signin import views
urlpatterns=[

  url('', views.login, name='login'),
  #path('dashboard/', views.dashboard, name='dashboard'),


]
