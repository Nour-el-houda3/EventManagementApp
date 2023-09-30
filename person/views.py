from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
def login_user(req):
    if req.method=='POST':
        username= req.POST['username']
        pwd= req.POST['password']

        user = authenticate( req , usermane = usermame, password = pwd)
        if user is not None:
            login(req,user)
            return redirect ("Affiche")
        else:
            messages.info(req,'Usernane or PwD Incorrect')
            return redirect('login')
    else:
        return render(req,'login.html')