from django.shortcuts import render
from .models import Place
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Home(View):
    def get(self, request):
        return HttpResponse("Wayfarer Home")



