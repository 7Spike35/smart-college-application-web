from django.shortcuts import render
from user.models import User
# Create your views here.



def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User()
        user.username = username
        user.email = email
        user.password = password
        user.save()
    return render(request,'user/register.html')
