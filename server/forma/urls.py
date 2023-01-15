from django.urls import path

from forma.views import get_all_forms, get_form
urlpatterns = [
    path('',  get_all_forms,  name='home'),
    path('get_form/', get_form, name='get_forms'),
]
