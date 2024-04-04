################################AuthMenu.py################################################
import os,time
import UserSqlConnect as USC
import mysql.connector as mysql
import MenuAfterLogin as MAL
import sys
import AdminAccess

def authMenu():

    #trying to create database if donot exist in admin system
    databaseCreated=False
    print("-----------------WELCOME to Code Manch-------------------")
    
    sqlp='please enter you MYSQL password here'##system's sql password
    try:
        AdminAccess.installer(sqlp)
    except Exception as e:
        #print("Already Created")
        databaseCreated=True
    try:
        ch=int(input("1. Login\n2. To register a new account\n3. About\n4. Exit\n-->"))
        if ch==1:
            os.system('cls')
            v=USC.loginUser(sqlp)
            log,uid=v##unpacking the tuple returned by login
            if log=="logsuccess":
                os.system('cls')
                MAL.afterLog(sqlp,uid)
                os.system('cls')
                authMenu()

                
            elif log=="logfail":
                os.system('cls')
                authMenu()
        elif ch==2:
            os.system('cls')
            uid=USC.registerUser(sqlp)###accessing uid to create table for new user
            #print(type(uid),'-',uid)
            if uid !='FailedReg':
                mydb=mysql.connect(username="root",passwd=sqlp,host="localhost",database="codecs")
                mycursor=mydb.cursor()###connecting to database
                query="create table {} (qid varchar(3)default (0),status int default (0) ,memory varchar(5) default (0))".format(uid)
                ##inserting the fields for user to maintain records
                mycursor.execute(query)
                mydb.commit()
                query="insert into {} (qid) values\
                ('LA1'),('LA2'),('LA3'),('LA4'),('LA5'),('LB1'),('LB2'),('LB3'),('LB4'),('LB5'),('LC1'),('LC2'),('LC3'),('LC4'),('LC5')".format(uid)
                mycursor.execute(query)
                mydb.commit()
                os.system('cls')
                MAL.afterLog(sqlp,uid)
                os.system('cls')
                authMenu()
            else:
                authMenu()

        elif ch==3:
            os.system('cls')
            print("CodeManch v1.1 : An initiative by Goel Bros for aiding Python learners")
            print("The app is loaded with the following features:")
            print("1.User interface for account registration and authentication\
            \n2.Assignment of randomly generated IDs for the users\
            \n3.Encryption of user credentials for security\
            \n4.Creation of unique database for the specified user\
            \n5.Menu for the user to perform the desired operation,viz.,checking the progress,solving more questions,logging out of the application\
            \n6.Assigning level,progress bar and star rating to each user as per the questions solved.\
            \n7Allowing the users to view only the questions belonging to their current level.\
            \n8.Taking the input from the user and executing it and running our predefined sample input to check the accuracy of the code\
            \n9.Calculation of time taken to write the code along with the memory occupied by the code")
            ch=input("PRESS ENTER TO CONTINUE")
            os.system('cls')
            authMenu()
        elif ch==4:
            sys.exit()
        else:
            print("Please enter a valid choice")
            time.sleep(1.5)
            os.system('cls')
            authMenu()  
    
    except ValueError:
        print("Please enter a valid choice")
        time.sleep(1.5)
        os.system('cls')
        authMenu()
    


'''
LA1
LA2
LA3
LA4
LA5
LB1
LB2
LB3
LB4
LB5
LC1
LC2
LC3
LC4
LC5
'''
