from django.shortcuts import render
from info.models import UserProfile
# Create your views here.

def historyinfo(request):
    return render(request, 'history/historyinfo.html')

def history(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            res = UserProfile.objects.filter(email=email)[0]
        return render(request, 'history/historyinfo.html', {'res': res.finalinfo})

    return render(request,'history/historypage.html')