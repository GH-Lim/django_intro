from django.shortcuts import render
import random


# Create your views here.
def index(request):         # 첫번쨰 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html' 을 보여준다.
    # 어디서?  =>  pages(소속된 앱) 안에 있는 templates 폴더
    return render(request, 'index.html') # render의 첫번째 인자도 반드시 request가 들어간다


def introduce(request):
    return render(request, 'introduce.html')


# Template Variable Example
def dinner(request):
    # 특정 변수를 html 에 전달을 해봅시다.
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick
    }
    # Django templates 로 context 전달
    return render(request, 'dinner.html', context)
