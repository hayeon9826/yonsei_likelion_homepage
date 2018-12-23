from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Homepage
# Create your views here.

def index(request):
    template = loader.get_template('homepage/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request,'homepage/about.html',{}) 
    