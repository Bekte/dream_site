from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('courses/<int:course_id>/', courses),
    path('teachers/', teachers),
    path('news/', news),
    path('gallery/', gallery),
    path('tests/', dream_tests),
]