from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def indexPage(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

