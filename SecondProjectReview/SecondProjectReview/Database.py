'''
Created on 03-Apr-2018

@author: Owner
'''
import sqlite3
from SecondProjectReview.MyConfig import databaseLocation

class Database:
    
    def GetUserTable(self):
        conn=sqlite3.connect(databaseLocation)
        curs=conn.cursor()
        curs.execute('''SELECT * FROM USER''')
        userTableData=curs.fetchall()
        print(userTableData)
        conn.close()
        return(userTableData)
    
    def CreateUserRecord(self,userId,name,emailId,phoneNumber,password):
        conn=sqlite3.connect(databaseLocation)
        curs=conn.cursor()
        curs.execute('''INSERT INTO USER(userId,name,emailId,phoneNumber,password) VALUES(?,?,?,?,?)''',(userId,name,emailId,phoneNumber,password))
        conn.commit()
        conn.close()
        
    def GetUser(self,phoneNumber,password):
        conn=sqlite3.connect(databaseLocation)
        curs=conn.cursor()
        curs.execute('''SELECT * FROM USER WHERE PHONENUMBER = ? and PASSWORD = ?''',(phoneNumber,password))
        userData=curs.fetchall()
        print(userData)
        conn.close()
        return(userData)
        
if __name__=="__main__":
    databaseObj=Database()
    #databaseObj.GetUserTable()
    #databaseObj.GetUser("1212121212","manisaran")