from django.shortcuts import render
from .utils import answer_1
from .utils import answer_2


def question(request):
    advice1 = ''
    advice2 = ''
    if request.method == 'POST':
        if 'code' in request.POST:
            code = request.POST.get('code')
            if code:
                advice1 = answer_1(code)
        elif 'name' in request.POST:
            name = request.POST.get('name')
            if question:
                advice2 = answer_2(name)
    return render(request, 'questions/questionpage.html', {'advice1': advice1, 'advice2': advice2})
