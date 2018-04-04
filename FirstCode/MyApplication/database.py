'''
Created on 24-Mar-2018

@author: Owner
'''
'''
Created on 18-Mar-2018

@author: Owner
'''
import sqlite3;
from sqlite3 import Error
import string
from builtins import int


class Database:
    def create_Table(self):
        conn=sqlite3.connect("F:\\eclipse\db\TrialDataBase.db")
        curs=conn.cursor()
        curs.execute("CREATE TABLE USERLOGIN(USERLOGINID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, PASSWORD TEXT, MAILID TEXT UNIQUE CHECK(MAILID like '%_%@%.%'), PHONENUMBER INTEGER UNIQUE CHECK(LENGTH(PHONENUMBER)==10))")
        conn.commit()
        conn.close()

    def Insert_Data(self,name,password,emailId,mobileNumber):    
        conn=sqlite3.connect("F:\\eclipse\db\TrialDataBase.db")
        curs=conn.cursor()
        curs.execute('''INSERT INTO USERLOGIN(NAME,PASSWORD,MAILID,PHONENUMBER) VALUES(?,?,?,?)''',(name,password,emailId,mobileNumber))
        conn.commit()
        conn.close()
    def Select_Data(self,tableName):
        conn=sqlite3.connect("F:\\eclipse\db\TrialDataBase.db")
        curs=conn.cursor()
        curs.execute('''SELECT * FROM '''+tableName)
        rows=curs.fetchall()
        #print(rows)
        conn.close()
        return(rows)
    def Update_Data(self,sourceValue,targetvalue):
        conn=sqlite3.connect("F:\\eclipse\db\TrialDataBase.db")
        curs=conn.cursor()
        curs.execute('''UPDATE USERLOGIN SET NAME = ? where USERLOGINID = ?''',(targetvalue,sourceValue))
        conn.commit()
        conn.close()
    def Update_Password(self,sourceValue,targetvalue):
        conn=sqlite3.connect("F:\\eclipse\db\TrialDataBase.db")
        curs=conn.cursor()
        curs.execute('''UPDATE USERLOGIN SET PASSWORD = ? where USERLOGINID = ?''',(targetvalue,sourceValue))
        conn.commit()
        conn.close()    
    def Drop_Table(self):
        conn=sqlite3.connect("F:\\eclipse\db\TrialDataBase.db")
        curs=conn.cursor()
        curs.execute('''DROP TABLE USERLOGIN''')
        conn.commit()
        conn.close()
    
    def GetUser(self,phoneNumber,password):
        conn=sqlite3.connect("F:\\eclipse\db\TrialDataBase.db")
        curs=conn.cursor()
        curs.execute('''SELECT * FROM USERLOGIN where PHONENUMBER = ? and PASSWORD = ?''',(phoneNumber,password))
        rows=curs.fetchall()
        #print(rows)
        conn.close()
        return(rows)
        
    def ValidateUser(self,phoneNumber,password):
        obj=Database()
        rows=obj.GetUser(phoneNumber, password)
        if(rows.__len__() > 0):
            return(True)
        else:
            return(False)
    
    
if __name__ == "__main__":
    obj=Database()
    #obj.create_Table()
    #obj.Insert_Data("VATSAN","vatsan999","vatsan@gmail.com","9999999999")
    #Select_Data("USERLOGIN")
    #Update_Data(2,"MANISARAN")
    #Drop_Table()
    #rows=obj.GetUser(9999999999, "vatsan999")
    
    