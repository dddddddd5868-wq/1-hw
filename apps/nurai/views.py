from django.http import HttpResponse


def home(request):
    return HttpResponse('Nurai app works!')
