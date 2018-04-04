'''
Created on 03-Apr-2018

@author: Owner
'''
from django.http.response import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from SecondProjectReview.User import User

@csrf_exempt
def index(request):
    
    if request.method == 'POST' :
        phoneNumber = request.POST.get('phoneNumber')
        password = request.POST.get('password')
        userObj=User()
        userData=userObj.VerifyUser(phoneNumber, password)
        
        if(userData):
            if(len(userData)==1):
                user=userData[0] 
                context = {
                    'userId':user[0],
                    'name':user[1],
                    'emailId':user[2],
                    'phoneNumber': user[3]            
                    }
                template = loader.get_template('ShowData.html')
                return HttpResponse(template.render(context, request))
               
            else:
                print("inside first if")
                template=loader.get_template('WrongCredentials.html')
                return HttpResponse(template.render())
        else:
            print("inside second if")
            template=loader.get_template('WrongCredentials.html')
            return HttpResponse(template.render())
            
        
    else:
        template=loader.get_template('LoginPage.html')
        return HttpResponse(template.render())
        
    