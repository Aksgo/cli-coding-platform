import mysql.connector as mysql
import os,time
import UserMenu
import QuesMenu
def afterLog(sqlp,uid):
    '''this function provides the menu to choose the option to view progress, do questions or logout'''

    mydb=mysql.connect(username="root",passwd=sqlp,host="localhost",database="codecs")
    mycur=mydb.cursor()
    mycur.execute(("select username from users where uid='{}'").format(uid))
    username=mycur.fetchall()[0][0]##fetching username to welcome
    print(("WELCOME {}".center(50,'=')).format(username))
    print("Enter 1, 2, or 3 to choose: ")
    print("1. View Progress Report")
    print("2. Solve Questions")
    print("3.Logout")
    try:
        ch=int(input("Enter your choice: "))
        if ch==3:#if user choose to logout , return to authmenu , which restarts program
            return 'AuthMenu'
        elif ch==1:
            os.system('cls')
            UserMenu.progressDisplay(sqlp,uid,15)# in case user wants to see progress
        elif ch==2:
            os.system('cls')
            QuesMenu.quesMenu(sqlp,uid)
            ch=input("\nPRESS ENTER TO GO BACK TO MAIN SCREEN")
            os.system('cls')
            afterLog(sqlp,uid)
        else:
            print("Please given valid option")#in case wrong integer given
            time.sleep(1.5)
            os.system('cls')
            afterLog(sqlp,uid)
    except ValueError:
        print("Please given valid option")#if any other data type
        time.sleep(1.5)
        os.system('cls')
        afterLog(sqlp,uid)

