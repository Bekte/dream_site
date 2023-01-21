from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('course/', course),
    path('teachers/', teachers),
    path('news/', news),
    path('gallery/', gallery),
    path('transfer_test/', transfer_test),
    path('form/', form),
]