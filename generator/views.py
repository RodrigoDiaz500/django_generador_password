from django.shortcuts import render
import random 

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.POST.get('length'))
    if request.POST.get('uppercase'): 
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.POST.get('special'):  
        characters.extend(list('!#$%&/?¡*+-¿'))
    if request.POST.get('numbers'):  
        characters.extend(list('0123456789'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})
