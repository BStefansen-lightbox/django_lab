from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question
from .serializers import ItemSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def foobar(request):
    return HttpResponse("foobar fizz buzz")

def squared(request):
    num = int(request.GET.get("number"))
    result = num**2
    return HttpResponse(f"Result: {result}")

 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
    }
 
    return Response(api_urls)
