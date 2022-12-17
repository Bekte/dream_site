from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = ["Курсы", "Учителя", "Новости", "Галерея", "Тесты"]


def index(request):
    return render(request, 'dream/index.html', {'memu': menu, 'title': 'American Dream Osh'})


def courses(request, course_id):
    return render(request, 'dream/course.html', {'memu': menu, 'title': 'American Dream Osh'})


def teachers(request):
    return render(request, 'dream/teachers.html', {'memu': menu, 'title': 'American Dream Osh'})


def news(request):
    return render(request, 'dream/news.html', {'memu': menu, 'title': 'American Dream Osh'})


def gallery(request):
    return render(request, 'dream/gallery.html', {'memu': menu, 'title': 'American Dream Osh'})


def dream_tests(request):
    return HttpResponse('TESTS')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не ннайдена</h1>')

