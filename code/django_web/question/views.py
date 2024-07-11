from django.shortcuts import render
from .utils import answer_1
from .utils import answer_2


def question1(request):
    advice = ''
    if request.method == 'POST':
        code = request.POST.get('code')
        if code:
            advice = answer_1(code)
    return render(request, 'question/questionpage.html', {'advice': advice})


def question2(request):
    advice = ''
    if request.method == 'POST':
        code = request.POST.get('code')
        if code:
            advice = answer_2(code)
    return render(request, 'question/questionpage.html', {'advice': advice})
