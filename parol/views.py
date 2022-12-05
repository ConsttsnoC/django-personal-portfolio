from django.shortcuts import render
import random


def password_home(request):
    return render(request,'parol/password_home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Верхний регист'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Специальные знаки'):
        characters.extend(list('!"#$%&()*+,-./:;<=>?@[\]_{}'))
    if request.GET.get('Цифры'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'parol/password.html',{'password':thepassword})
