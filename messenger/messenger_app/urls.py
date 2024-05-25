from django.urls import path
from .views import index, save_text, login, register, logout, remove_text, edit_text


urlpatterns = [
    path('', index, name='index'),
    path('save_text/', save_text, name='save_text'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('edit_text/<int:text_id>', edit_text, name='edit_text'),
    path('remove_text/<int:text_id>', remove_text, name='remove_text'),
]