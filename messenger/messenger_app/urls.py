from django.urls import path
from .views import index, save_text, login


urlpatterns = [
    path('', index, name='index'),
    path('save_text/', save_text, name='save_text'),
    path('login/', login, name='login'),
]