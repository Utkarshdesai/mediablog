from django.http import HttpResponse


def blog(request):
     return HttpResponse("<h1>Welcome to Chai's Django Project: welcome page</h1>")