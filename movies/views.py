from django.http import HttpResponse

def movie_list(request):
    return HttpResponse("Your Movies App Works!")
