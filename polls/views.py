from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Youŕe at the polls index.")

# Create your views here.