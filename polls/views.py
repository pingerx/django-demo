from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("welcome，you are at the polls index.")
