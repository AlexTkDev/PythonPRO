from django.shortcuts import render

# Create your views here.


def is_auntification(request):
    message = {"message": f"Авторизованный пользователь: {request.user.username}"}
    if request.user.is_anonymous:
        message.update({"message": "Анонимный пользователь, авторизуйтесь!"})
        return render(request, "auntification_information.html", message)
    return render(request, "auntification_information.html", message)
