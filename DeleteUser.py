import mysql.connector as mysql
from os import system
import time
def deleteUsers(pass_sql):
    try:
            
        mydb=mysql.connect(username="root",passwd=pass_sql,host="localhost",database="codecs")
        mycursor=mydb.cursor()
        queryTables="show tables"
        mycursor.execute(queryTables)
        data=mycursor.fetchall()
        for i in data:
            uid=i[0]
            mycursor.execute("select uid,username,password from users\
            where uid='{}'".format(uid))
            
            record=mycursor.fetchone()
            
            uidn,user,passw=record
            ch=input("Do you want to delete 'uid': {0},'username': {1}->(y/n/b(stopDelete)):".format(uidn,user,passw))
            if ch =='y':
                mycursor.execute("delete from users where uid='{}'".format(uidn))
                mycursor.execute("drop table {}".format(uidn))
                print("record deleted successfully")
            elif ch=='b':
                print("Deletion Terminated")
                break
            else:
                print("Record deletion failed")
    except Exception as e:
        print(e)
        return 'done'
deleteUsers('admin123')
time.sleep(5)
