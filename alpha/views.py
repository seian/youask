from django.http import HttpResponse
from django.template import loader

#########
from .models import Members ##to Try connecting View.py and Models.py
from django.shortcuts import render, get_object_or_404, redirect
#########

def index(request):
    template = loader.get_template('alpha/index.html')

    return HttpResponse(template.render(None, request))


def thread(request):
    template = loader.get_template('alpha/thread.html')

    return HttpResponse(template.render(None, request))


##########
def members_list(request):
    members = Members.objects.all()
    context = {
        "object_list" : members,
    }
    return render(request, 'alpha/showmembers.html',context)
#########
