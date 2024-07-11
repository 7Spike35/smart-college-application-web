from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from user.models import User
from django.shortcuts import render, reverse,redirect
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email)[0]
        if password == user.password:
            return redirect('home')
        else:
            return HttpResponse('登录失败')
    return render(request,'login/loginpage.html')