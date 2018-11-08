from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from signup.models import registeration
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
	context = {}
	if request.method=='POST':
		rusername=request.POST['username']
		print(rusername)
		rpassword=request.POST['password']
		print(rpassword)

		recking = registeration.objects.get(dusername=rusername)
		reck=check_password(rpassword, recking.dpassword)
		print(reck)
	

		#if reec:
		#	context={"message": "login"}
		#else:
			#context={"message": "wrong username and password"}


	return render(request, 'signin/login.html', context)




#@login_required(login_url='/signin/')
#def dashboard(request):
 #  context={}
   #return render(request, 'signin/dashboard.html', context) 															
