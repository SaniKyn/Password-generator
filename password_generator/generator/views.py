from django.shortcuts import render
import random


# request -

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')  # преход на главную страницу

def info(request):
    return render(request, 'generator/info.html')  # преход на страницу информации

def password(request):
    charaters = list('abcdefghijklmnopqrstuvwxyz')  # буквы в нижнем регистре
    # либо characters = list(string.ascii_lowercase)

    # создаем условие где при выборе Uppercase в home.html он добавлял в заглавные буквы
    if request.GET.get(
            'uppercase'):
        charaters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        # либо characters.extend(list(string.ascii_uppercase))

    # создаем условие где при выборе Special Characters в home.html он добавлял специальные символы
    if request.GET.get(
            'special'):
        charaters.extend(list('!@#$%^&*()'))

    # создаем условие где при выборе Numbers в home.html он добавлял цифры
    if request.GET.get(
            'numbers'):
        charaters.extend(list('1234567890'))
        # либо characters.extend((list(string.digits)))

    length = int(request.GET.get('length'))  # определяем длину
    thepassword = ''  # пустая строка для пароля

    # цикл для преребирание смоволов
    for x in range(length):
        thepassword += random.choice(charaters)  # рандомное смовольное добавление в страку thepassword

    # возращение результата на страницу password.html
    return render(request, 'generator/password.html', {'password': thepassword})
