from django.db import models

# Create your models here.
class registeration(models.Model):
	dfirstname=models.CharField(max_length=200)
	dlastname=models.CharField(max_length=200)
	dusername=models.CharField(max_length=200)
	dpassword=models.CharField(max_length=200)
	dconfirmpassword=models.CharField(max_length=200, default = "")
