from django.template import loader
from django.http import HttpResponse

# Create your views here.
def memberss(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


