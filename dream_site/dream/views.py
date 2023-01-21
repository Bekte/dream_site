from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'dream/index.html', {
        'page': 'home'
    })


def course(request):
    return render(request, 'dream/course.html', {
        'page': 'course'
    })


def teachers(request):
    return render(request, 'dream/teachers.html', {
        'page': 'teachers'
    })


def news(request):
    return render(request, 'dream/news.html', {
        'page': 'news'
    })


def gallery(request):
    return render(request, 'dream/gallery.html', {
        'page': 'gallery'
    })


def form(request):
    return render(request, 'dream/form.html')


def transfer_test(request):
    return render(request, 'dream/transfer_test.html', {
        'page': 'transfer_test'
    })


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Page not found </h1>')

