from django.conf.urls import url, include
from signup import views
urlpatterns=[

 url('', views.register, name='register'),
 

]
