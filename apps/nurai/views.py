from django.http import HttpResponse
from django.shortcuts import render

from .models import Student


def home(request):
    return HttpResponse('Nurai app works!')


def index(request):
    students = Student.objects.all()
    return render(request, "index.html", locals())
