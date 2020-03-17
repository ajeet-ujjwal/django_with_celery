from celery import shared_task
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import string
@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def create_random_users(num):
    for i in range(num):
        User.objects.create_user(username=get_random_string(15, string.ascii_letters))