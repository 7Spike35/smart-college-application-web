
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RecommendationForm
# Create your views here.
from django.shortcuts import render


def analy(request):
    return render(request,'info/analy.html')
def info(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            # 保存表单数据到数据库
            user_profile = form.save()
            # 可以重定向到另一个页面或显示成功消息
            return redirect('analy')
    else:
        form = RecommendationForm()
    return render(request, 'info/info.html', {'form': form})