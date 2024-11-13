from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.



from django.contrib.auth.hashers import make_password, check_password
from .models import UserRegistration, LoginTable



def Register(request):
    login_table=LoginTable()
    user_profile=UserRegistration()
    if request.method == "POST":
        user_profile.full_name = request.POST['full_name']
        user_profile.username = request.POST["username"]
        user_profile.email = request.POST["email"]
        user_profile.password = request.POST["password"]
        user_profile.cpassword = request.POST["password"]

        login_table.username=request.POST["username"]
        login_table.password=request.POST["password"]

        login_table.type='user'


        if request.POST["password"] == request.POST["password"]:
            user_profile.save()
            login_table.save()
            messages.info(request,"Registration Success")
            return redirect("authapp:login")
        else:
            messages.info(request,"Incorrect Password!")
            return redirect('authapp:register')
    return render(request, "authentication/register.html")



def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]


        #user =LoginTable.authenticate(username=username,password=password)
        user=LoginTable.objects.filter(username=username,password=password,type='user').exists()
        # try:
        if user is not None:
            user_details=LoginTable.objects.get(username=username,password=password)
            user_name=user_details.username
            type=user_details.type

            if type=='user':
                request.session['username']=username
                return redirect('userapp:user_booklist')
            elif type=='admin':
                request.session['username']=username
                return redirect('bookapp:admin_booklist')
        else:
            messages.info(request,'invalid username or password')
        # except:
        #     messages.error(request,'invalid role')
    return render(request,'authentication/login.html')




def logOut(request):
    auth.logout(request)
    return redirect('login')


