from django.shortcuts import render


def is_auntification(request):
    context = {"message": f"Авторизованный пользователь: {request.user.username}"}
    if request.user.is_anonymous:
        context.update({"message": "Анонимный пользователь, авторизуйтесь!"})
        return render(request, "auntification_information.html", context)
    return render(request, "auntification_information.html", context)

