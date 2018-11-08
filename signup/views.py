from django.shortcuts import render

# Create your views here.
from .models import registeration
def register(request):
	context={}
	if request.method=='POST':
		fname=request.POST["fname"]
		lname=request.POST["lname"]
		fusername=request.POST["username"]
		fpassword=request.POST["password"]
		rpassword=request.POST["confirmpassword"]
		
		dsobj=registeration()
		dsobj.dfirstname=fname
		dsobj.dlastname = lname
		dsobj.dusername=fusername
		dsobj.dpassword=fpassword
		dsobj.dconfirmpassword=rpassword
		dsobj.save()
	return render(request, 'signup/register.html', context)



#def deletefunc(request,id):
#	registeration.objects.filter(id=id).delete
#	context={}
#	return render(request, 'signup/register.html', context)

