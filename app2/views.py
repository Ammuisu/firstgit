from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def isu(request):
    return HttpResponse('<h1><i>Isu is my cutest dog,Isu is my one of the family member,But I miss u Isu</h1></i>')
