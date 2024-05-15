from django.urls import path
from .views import input_information, show_information, index, remove_member


urlpatterns = [
    path("", index, name="index"),
    path("input/", input_information, name="input_information"),
    path("show/", show_information, name="show_information"),
    path("show/remove-member/<int:member_id>/", remove_member, name="remove_member")
]