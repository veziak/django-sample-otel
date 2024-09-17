from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader


def index(request):
    users = User.objects.all()
    print(users)
    template = loader.get_template('index.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))
