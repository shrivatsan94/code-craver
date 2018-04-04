import MyApplication.database
from django.contrib.auth import login

class User:
    def CreateUser(self,name,password,mailId,phoneNumber):
        databaseObj=MyApplication.database.Database()
        databaseObj.Insert_Data(name, password, mailId, phoneNumber)
        print("values injected successfully")
        return
        
    def RegisteredUser(self):
        print("Enter Your phonenumber")
        phoneNumber=input()
        print("Enter Your password")
        password=input()
        userObj=User()
        #userObj.VerifyUser(phoneNumber, password)
        rows=userObj.VerifyUser(phoneNumber, password)
        return(rows)
        
    def VerifyUser(self,phoneNumber,password):
        databaseObj=MyApplication.database.Database()
        if(databaseObj.ValidateUser(phoneNumber, password)):
            print("YOU HAVE SUCCESSFULLY LOGGED IN!!!")
            rows=databaseObj.GetUser(phoneNumber, password)
            #print(rows)
            values=rows[0]
            #print(values)
            print("your details:")
            print("userid:",values[0])
            print("user name:",values[1])
            print("mail id:",values[3])
            print("phone number:",values[4])
            return(rows)
        else:
            return(False)
        
            #print("user name or password is incorrect")
        #userObj.HomePage()
    
    def ChangePassword(self):
        databaseObj=MyApplication.database.Database()
        rows=userObj.RegisteredUser()
        values=rows[0]
        print("Enter your new password")
        newPassword=input()
        databaseObj.Update_Password(values[0], newPassword)
        print("Password changed successfully")
        userObj.VerifyUser(values[4], newPassword)
        userObj.HomePage()
        
        
        
        
    
    def HomePage(self):
        print("login or signup or changePassword")
        userInput=input()
        userObj=User()
        if(userInput=="login"):
            userObj.RegisteredUser()
        elif(userInput=="signup"):
            userObj.CreateUser()
        elif(userInput=="changePassword"):
            userObj.ChangePassword()
        else:
            print("invalid entry")  
            userObj.HomePage()     
            
        
        
if __name__ == "__main__":
    userObj=User()
    userObj.HomePage()
    
        
        
    
    

        
    
    
    