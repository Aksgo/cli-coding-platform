import mysql.connector as mysql
from os import system


def installer(pass_sql):

    mydb=mysql.connect(username="root",passwd=pass_sql,host="localhost")
    mycur=mydb.cursor()###connecting to database
    databaseQuery="create database codecs"
    mycur.execute(databaseQuery)#creating database codecs in admin mysql
    #connecting with database
    mydb=mysql.connect(username="root",passwd=pass_sql,host="localhost",database="codecs")
    mycursor=mydb.cursor()
    #creating table for users
    queryUsersTable="create table users(\
                    uid char(9) primary key not null,\
                    username char(20) not null,\
                    password char(20) not null)"
    mycursor.execute(queryUsersTable)
    #print("created Now")
    

