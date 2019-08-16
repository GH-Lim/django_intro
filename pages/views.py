from django.shortcuts import render
from datetime import datetime
import random


# Create your views here.
def index(request):         # 첫번쨰 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html' 을 보여준다.
    # 어디서?  =>  pages(소속된 앱) 안에 있는 templates 폴더
    return render(request, 'index.html') # render의 첫번째 인자도 반드시 request가 들어간다


def introduce(request):
    return render(request, 'introduce.html')


# Template Variable Example
def dinner(request, name):
    # 특정 변수를 html 에 전달을 해봅시다.
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name,
    }
    # Django templates 로 context 전달
    return render(request, 'dinner.html', context)


def image(request):
    image_url = 'https://picsum.photos/600/400.jpg'
    context = {
        'randimage': image_url,
    }
    return render(request, 'image.html', context)


def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'result': result,
    }
    return render(request, 'times.html', context)


def strtimes(request, numxnum):
    num1, num2 = map(int, numxnum.split('x'))
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 * num2,
    }
    return render(request, 'strtimes.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)


def isitbirthday(request):
    my_birthday = '0816'
    context = {
        'mybirthday': my_birthday,
    }
    return render(request, 'isitbirthday.html', context)


def isityourbirthday(request, birthday):
    your_birthday = birthday
    context = {
        'yourbirth': your_birthday,
    }
    return render(request, 'isityourbirthday.html', context)


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    rand_lotto = random.sample(range(1,46), 6)
    rand_lotto.sort()
    context = {
        'real_lotto': real_lotto,
        'lotto': rand_lotto,
    }
    return render(request, 'lotto.html', context)
