from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey Kaley, I love you!!")
