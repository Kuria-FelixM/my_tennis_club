# Create your views here
from django.template import loader
from django.http import HttpResponse
from .models import *


def memberss(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


