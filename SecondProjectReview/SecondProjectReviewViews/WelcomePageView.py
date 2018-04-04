'''
Created on 03-Apr-2018

@author: Owner
'''
from django.http.response import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    template= loader.get_template('WelcomePage.html')
    return HttpResponse(template.render())
    
    