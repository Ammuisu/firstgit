from django.shortcuts import render
from django.http import HttpResponse
#Create your views here.
def jyothi(request):
    return HttpResponse('<h1><i>We are In Jspider students</i></h1>')
def banu(request):
    return HttpResponse('<b><i><h1><marquee>Banu is my brother</b></marquee></i>')
