import os
import sys
import shutil
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings

def render_form(request):
    return render(request, 'success.html')

def confirm(request):
    name=request.GET.get('name','')
    mydir = os.path.realpath(name)
    if name == settings.SECRET_KEY:
        print('equal')
        mydir= 'test.txt'
    print(settings.SECRET_KEY)
    try:
        shutil.rmtree(mydir)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
    return render(request, 'pass.html')