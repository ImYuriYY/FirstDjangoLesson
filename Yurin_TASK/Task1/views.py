from django.shortcuts import render
from django.http import HttpResponse

def index(request, name, age, hobbies):
    return HttpResponse(f'Мои ФИО: {name}. Мне {age} лет. Интересы: {hobbies}')

def about(request, city, progress, likes):
    return HttpResponse(f'Я из города {city}, моя успеваемость {progress}, я {likes}')

def contacts(request, gith, vk):
    return HttpResponse(f'Мой гитхаб: {gith}, страница ВК: {vk}')
