from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the music index.")

def artists(request):
    return HttpResponse("Artists.")

def artist_details(request):
    return HttpResponse("Hello, world. Artist_Details.")