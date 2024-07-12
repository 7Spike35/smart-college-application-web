# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse
from .utils import result1, result2


def analy(request):
    return render(request, 'info/analy.html')


def info(request):
    if request.method == "POST":
        email = request.POST.get('email')
        score = request.POST.get('score')
        rank = request.POST.get('rank')
        subject = request.POST.getlist('subject')
        interest = request.POST.get('interest')

        # 尝试从数据库中获取 UserProfile 对象
        try:
            user = UserProfile.objects.get(email=email)
            # 如果找到了，就更新它
            user.score = score
            user.rank = rank
            user.subject = subject[0]  # 注意：这里假设 subject 是一个合适的字段来存储列表，否则你可能需要序列化它
            user.interest = interest
        except UserProfile.DoesNotExist:
            # 如果没有找到，就创建一个新的 UserProfile 对象
            user = UserProfile()
            user.email = email
            user.score = score
            user.rank = rank
            user.subject = subject[0]  # 同样，注意字段类型
            user.interest = interest

        answer1 = result1(rank, subject, interest)
        answer2 = result2(rank, subject, interest)
        user.finalinfo = answer2
        user.save()
        return render(request, 'info/analy.html', {'answer1': answer1, 'answer2': answer2})

        # 如果不是 POST 请求，可能是 GET 请求或其他，渲染表单页面
    return render(request, 'info/info.html')
