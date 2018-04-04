'''
Created on 24-Mar-2018

@author: Owner
'''
from django.http.response import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from MyApplication.database import Database
from MyApplication import User

@csrf_exempt
def index(request):
    #if post request came 
    if request.method == 'POST' :
        #getting values from post
        name=request.POST.get('name')
        phoneNumber = request.POST.get('phoneNumber')
        mailid=request.POST.get('email')
        password = request.POST.get('password')
        
        userObj=User()
        userObj.CreateUser(name,password,mailid,phoneNumber)
        print(phoneNumber)
        print(password)
        rows=userObj.VerifyUser(phoneNumber,password)
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
                template = loader.get_template('signedUp.html')
                return HttpResponse(template.render(context, request))
           
            else:
                template=loader.get_template('firstpage.html')
                return HttpResponse(template.render())
            #getting our showdata template
        except:
            template=loader.get_template('wrongcredentials.html')
            return HttpResponse(template.render())
    else:
        template= loader.get_template('signup.html')
        return HttpResponse(template.render())
    
    
    