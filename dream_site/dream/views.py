from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, 'dream/index.html')


def course(request):
    return render(request, 'dream/course.html')


def teachers(request):
    return render(request, 'dream/teachers.html')


def news(request):
    return render(request, 'dream/news.html')


def gallery(request):
    return render(request, 'dream/gallery.html')


def dream_tests(request):
    return HttpResponse('TESTS')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не ннайдена</h1>')

