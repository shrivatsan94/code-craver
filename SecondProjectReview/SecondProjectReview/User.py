'''
Created on 03-Apr-2018

@author: Owner
'''
'''
Created on 28-Mar-2018

@author: Owner
'''
import re
import SecondProjectReview.Database
from itertools import count
from SecondProjectReview.Database import Database

class User:
        
    def GetUserName(self):
        return self.name
    
    def GetPhoneNumber(self):
        return self.phoneNumber
    
    def GetEmailId(self):
        return self.emailId
    
    def GetPassword(self):
        return self.password
    
    def SetUserId(self):
        userId=self.CreateUserId()
        self.userId=userId
    
    def SetUserName(self,name):
        if(self.ValidateUserName(name)):
            self.name=name
        
    def SetPhoneNumber(self,phoneNumber):
        if(self.ValidatePhoneNumber(phoneNumber)):
            self.phoneNumber=phoneNumber
        
    def SetEmailId(self,emailId):
        if(self.ValidateEmailId(emailId)):
            self.emailId=emailId.lower()
            
    def SetPassword(self,password):
        if(self.ValidatePassword(password)):
            self.password=password
        
    def ValidateUserName(self,name):
        if (re.match("^[a-zA-Z0-9_]*$",name)):
            return True
        else:
            print("user name is wrong")
            return False
            
    def ValidatePhoneNumber(self,phoneNumber):
        userPhoneNumberList=list()
        databaseObj=Database()
        userTableData=databaseObj.GetUserTable()
        userTableLength=userTableData.__len__()
        
        if(re.findall(("[\d]{10}"),phoneNumber)):
            for i in range(userTableLength):
                userData=userTableData[i]
                userPhoneNumberList.insert(i,userData[3])
                
            if(phoneNumber not in userPhoneNumberList):
                return True
            else:
                print("phone number1 is wrong")
                return False
            
        else:
            print("phone number2 is wrong")
            return False
        
    def ValidateEmailId(self,emailId):
        emailIdPattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
        userEmailIdList=list()
        databaseObj=Database()
        userTableData=databaseObj.GetUserTable()
        userTableLength=userTableData.__len__()
        
        if(re.match(emailIdPattern,emailId)):
            for i in range(userTableLength):
                userData=userTableData[i]
                userEmailIdList.insert(i,userData[2].lower())
                
            if(emailId.lower() not in userEmailIdList):
                return True
            else:
                print("emailId1 is wrong")
                return False
            
        else:
            print("emailId2 is wrong")
            return False
    
    def ValidatePassword(self,password):
        passwordPattern=r'[a-zA-Z0-9@#$%^&+=]{8,}'
        if(re.match(passwordPattern,password)):
            return True
        else:
            print("password is wrong")
            return False
    
    def CreateUserId(self):
        userIdList=list()
        databaseObj=Database()
        userTableData=databaseObj.GetUserTable()
        userTableLength=userTableData.__len__()
        
        for i in range(userTableLength):
            userData=userTableData[i]
            userIdList.insert(i,userData[0])
        
        for i in range(userTableLength-1):
            if(userIdList[i]<userIdList[i+1]):
                lastUserId=userIdList[i+1]
        
        nextUserId=str(int(lastUserId)+1).zfill(6)
        print(nextUserId)
        return nextUserId
    
    def VerifyUser(self,phoneNumber,password):
        databaseObj=Database()
        userData=databaseObj.GetUser(phoneNumber, password)
        userDataLength=userData.__len__()
        
        if(userDataLength>0):
            return userData
        else:
            return False
            
    def CreateUser(self,name,emailId,phoneNumber,password):
        databaseObj=Database()
        self.SetUserId()
        self.SetUserName(name)
        self.SetEmailId(emailId)
        self.SetPhoneNumber(phoneNumber)
        self.SetPassword(password)
        databaseObj.CreateUserRecord(self.userId,self.name,self.emailId,self.phoneNumber,self.password)
        
if __name__=="__main__":
    userObj=User()
    #print(userObj.ValidatePhoneNumber("6767676767"))
    #print(userObj.ValidateEmailId("arsan@gmail.com"))
    #print(userObj.ValidatePassword("tamilarasan"))
    #userObj.CreateUserId()
    