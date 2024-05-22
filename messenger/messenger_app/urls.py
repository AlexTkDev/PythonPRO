from django.urls import path
from .views import index, save_text


urlpatterns = [
    path('', index, name='index'),
    path('save_text/', save_text, name='save_text'),
]