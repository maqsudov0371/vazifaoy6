from django.shortcuts import render
from . import models

def watches(request):
<<<<<<< HEAD
    posts = models.Watches.objects.all()
    context = {
        'posts':posts
    }
    
    return render(request, 'watches.html', context)


def register_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        user = models.User.objects.create(
            username = name,
            email = email
        )
        user.set_password(password)
        user.save()

    return render(request, 'register.html') 


def appeals(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        appeal = request.POST['appeals']

        appeals = models.Appeal.objects.create(
            username = name,
            email = email,
            appeal = appeal
        )
        appeals.save()
    return render(request, 'appeals.html')
=======
    return render(request, 'watches.html')
>>>>>>> 67deb43ece3e734db73ed23888567b8c2e9c3b75
