from django.shortcuts import render
from .tasks import create_random_users
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    users = User.objects.all()
    if request.POST:
        num_users = request.POST.get('num_users')
        print(num_users)
        create_random_users.delay(int(num_users))
        messages.add_message(request, messages.SUCCESS, 'New users are being created')
    return render(request, 'users/index.html', {'users': users})
