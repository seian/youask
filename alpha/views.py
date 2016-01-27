from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('alpha/index.html')

    return HttpResponse(template.render(None, request))


def thread(request):
    template = loader.get_template('alpha/thread.html')

    return HttpResponse(template.render(None, request))

 