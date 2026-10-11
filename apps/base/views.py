from django.http import HttpResponse


def home(request):
    return HttpResponse('Love project works!')
