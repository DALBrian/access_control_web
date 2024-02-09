from django.shortcuts import render
from .models import User

def add_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_image = request.FILES.get('user_image')
        user_image2 = request.FILES.get('user_image2')
        user = User(user_name=user_name, user_image=user_image, user_image2=user_image2.read())
        user.save()
        return render(request, 'add_user.html', locals())
    return render(request, 'add_user.html', locals())

def user_detail(request):
    list_user = User.objects.all()
    return render(request, 'user_detail.html', locals())
                  