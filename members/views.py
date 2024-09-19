# views
from django.template import loader
from django.http import HttpResponse
from .models import *
from .serializers import *


def memberss(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


