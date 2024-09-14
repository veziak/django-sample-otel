from django.contrib.auth.models import User
from django.http import HttpResponse


def index(request):
    users = User.objects.all()
    return HttpResponse("Hello, world. You're at the polls index.")
