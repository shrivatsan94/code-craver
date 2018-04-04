'''
Created on 04-Apr-2018

@author: Owner
'''
from django.http.response import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from SecondProjectReview.User import User

@csrf_exempt
def index(request):
    if request.method == 'POST' :
        #getting values from post
        name=request.POST.get('name')
        emailId=request.POST.get('emailId')
        phoneNumber = request.POST.get('phoneNumber')
        password = request.POST.get('password')
        
        try:
            userObj=User()
            userObj.CreateUser(name,emailId,phoneNumber,password)
            userData=userObj.VerifyUser(phoneNumber,password)
            if(userData):
                if(len(userData)==1):
                    user=userData[0]
                    #adding the values in a context variable 
                    context = {
                        'userId':user[0],
                        'name':user[1],
                        'emailId':user[2],
                        'phoneNumber': user[3]            
                        }
                    template = loader.get_template('ShowData.html')
                    return HttpResponse(template.render(context, request))
               
                else:
                    template=loader.get_template('WrongCredentials.html')
                    return HttpResponse(template.render())
                
            else:
                template=loader.get_template('WrongCredentials.html')
                return HttpResponse(template.render())
        except:
            template=loader.get_template('WrongCredentials.html')
            return HttpResponse(template.render())
            
    else:
        template= loader.get_template('SignUpPage.html')
        return HttpResponse(template.render())