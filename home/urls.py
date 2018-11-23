from django.conf.urls import url, include
from home import views
urlpatterns=[
   
    url('', views.home, name='home'),
]
