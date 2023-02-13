from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def foobar(request):
    return HttpResponse("foobar fizz buzz")
