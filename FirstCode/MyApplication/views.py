'''
Created on 23-Mar-2018

@author: Owner
'''
from django.http.response import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from MyApplication.database import Database
from MyApplication import User
import MyApplication


@csrf_exempt
def index(request):
    
    if request.method == 'GET' :
        template= loader.get_template('firstpage.html')
        return HttpResponse(template.render())
        
    
    #if post request came 
    if request.method == 'POST' :
        #getting values from post
        
        phoneNumber = request.POST.get('phoneNumber')
        password = request.POST.get('password')
        
        userObj=User()
        
        rows=userObj.VerifyUser(phoneNumber, password)
        try:
            if(rows.__len__() > 0):
                values=rows[0]
                #adding the values in a context variable 
                context = {
                    'loginid':values[0],
                    'name':values[1],
                    'mailid':values[3],
                    'phoneNumber': values[4]            
                    }
                template = loader.get_template('showdata.html')
                return HttpResponse(template.render(context, request))
           
            else:
                template=loader.get_template('firstpage.html')
                return HttpResponse(template.render())
            #getting our showdata template
        except:
            template=loader.get_template('wrongcredentials.html')
            return HttpResponse(template.render())
            
    
        #returing the template 
        

        #if post request is not true 
        #returing the form template 
        