from django.template import loader
from django.http import HttpResponse

# views
def memberss(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

# Create your views here.
