from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *

# Create your views here.

def platform(request):
    title = 'мой сайт'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'first_task/platform.html', context)

def games(request):
    Games = Game.objects.all()
    contex = {'games': Games}
    return render(request, 'first_task/games.html', contex)

def cart(request):
    return render(request, 'first_task/cart.html')

def menu(request):
    return render(request, 'first_task/menu.html')

def sign_up_by_html(request):
    Buyers = Buyer.objects.all()
    info = {'error': None}
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        second_password = request.POST.get('second_password')
        age = request.POST.get('age')
        if int(age) < 18:
            info['error'] = 'Возраст не менее 18'
        elif password != second_password:
            info['error'] = 'Пароли не совпадают'
        elif login in Buyers:
            info['error'] = 'Данный пользователь уже существует'
        else:
            Buyers.append(login)
            return HttpResponse(f'Приветствуем, {login}')
    context = {
        'info': info['error']
    }
    return render(request, 'first_task/registration_page.html', context)

def sign_up_by_django(request):
    Buyers = Buyer.objects.all()
    info = {'error': None}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            second_password = form.cleaned_data['second_password']
            age = form.cleaned_data['age']

            for buyer in Buyers:
                print(buyer.name, login, buyer.name == login)
                if login.lower() == buyer.name.lower():
                    info['error'] = 'Данный пользователь уже существует'
                    break
                elif password != second_password:
                    info['error'] = 'Пароли не совпадают'
            if info['error'] == None:
                Buyer.objects.create(name=login, balance=100, age=age)
                return HttpResponse(f'Приветствуем, {login}')
    else:
        form = UserRegister()
    context = {
        'Buyers': Buyers,
        'form': form,
        'info': info['error']
    }
    return render(request, 'first_task/registration_page.html', context)














