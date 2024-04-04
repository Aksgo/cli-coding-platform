
import mysql.connector as mysql
from time import sleep
from getpass import getpass#to get password
import random
from os import system
from Security import encrypt,decrypt
'''name='tbd'
welcome="Welcome to "+name
print(welcome.center(100,'-'))###welcome message
'''

def registerUser(pass_sql):
    
    '''function to register new user to sql'''

    mydb=mysql.connect(username="root",passwd=pass_sql,host="localhost",database="codecs")
    mycursor=mydb.cursor()
    
    mycursor.execute("select uid from users")
    data=mycursor.fetchall()
    ##extracting uid for checking and giving unique to user

    print("-----------------NOTE : password may not be visible while typing-----------------")
    username=input("Enter username:")

    #taking password input
    password=getpass(prompt="Enter new password : ")
    password_confirm=getpass(prompt="Confirm new password: ")

    #generating unique id after passowrd confirmation
    if password == password_confirm:
        #encrpyting password
        enc_pass,key=encrypt([password])
        passwordEnc=enc_pass[0]+str(key[0])
        ##passwordEnc is the string with last two chracters as key that i s[-2:]
        while True:
            uid_int=random.randint(100000,999000)
            uid='uid'+str(uid_int)
            if (uid,) not in data:#uid will be in a tuple in 'data' object
                break
        ##inserting the records of user in users table in mysql database
        mycursor.execute("insert into users values('{0}','{1}','{2}')".format(uid,username,passwordEnc))
        mydb.commit()
        sleep(0.5)
        print("Successfully registered".center(30,'-'))
        print("Your unique user id : ",uid)
        print("NOTE : please note the unique id as you may need it while login")
        cont=input("PRESS ENTER TO CONTINUE")
        return uid
    

    ##if passord confirmation fails, the revert back to username
    else:
        print("!!!!!!!Password Confirmation Failed!!!!!!!")
        sleep(0.5)
        ###confirmation to register again after failed registeration
        ch=input("Do you want to register again (y/n): ")
        if ch.lower()=='y':
            print("Reverting Back")
            sleep(1)
            system('cls')
            return registerUser(pass_sql)
            
        else:
            system('cls')
            return "FailedReg"

        
#registerUser('admin123')#typeyour sql password in argument

# if user selects to login
def loginUser(pass_sql):
    '''function to login the user by checking
     the uid and password in database'''
    print("***PASSWORD IS HIDDEN DUE TO SECURITY REASONS***")
    mydb=mysql.connect(username="root",passwd=pass_sql,host="localhost",database="codecs")
    mycursor=mydb.cursor()###connecting to database
    uid=input("unique id: ")###accepting unique id
    password=getpass(prompt="Password: ")##accepting password
    detail=(uid,password)##packed them in a tuple

    mycursor.execute("select uid, password from users")##extracting data from users table in codecs database
    found=0##initalized given details not found
    while True:
        data=mycursor.fetchone()##accessing each detail instead of loading whole set

        if data!=None:# and data==detail:##if details match with no None type then user logged in successful
            passw_data=data[1]
            #decrypting password first
            pass_key=[int(passw_data[-2:])]#accessing the key for decryption
            passw_str=[passw_data[:-2]]#accessing password for decrytion
            decryptedPassw=decrypt(passw_str,(pass_key))#decrypted password is returned as list 
            tuple1=(data[0],decryptedPassw[0])#storing uid and decrypted password in a tuple to compare with input tuple
            if tuple1==detail:
                found=1
                break
            else:
                continue#entries still left to check
        else:
            #data=None--if all the data read and received None object
            found=0
            break
            
    if found==1:
        print("Login Success".center(50,'='))
        sleep(1.5)
        return "logsuccess",uid
    else:
        print("Login Failed".center(50,'='))
        sleep(1.5)
        return "logfail",uid

#loginUser('admin123') ##type your mysql paasword

