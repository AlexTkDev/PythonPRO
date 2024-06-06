from django.urls import path
from .views import (
    IndexView,
    SaveTextView,
    EditTextView,
    RemoveTextView,
    LoginView,
    RegisterView,
    LogoutView,
    get_user_status
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('save_text/', SaveTextView.as_view(), name='save_text'),
    path('edit_text/<int:text_id>/', EditTextView.as_view(), name='edit_text'),
    path('remove_text/<int:text_id>/', RemoveTextView.as_view(), name='remove_text'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('status/<str:username>/', get_user_status, name='get_user_status'),

]
