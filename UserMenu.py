###############################################################UserMenu.py################################################
import mysql.connector as mysql
import time,os
import MenuAfterLogin as MAL
def progressDisplay(pass_sql,uid,totalQues):

    '''this function is used to display the progress bar\
    and the start level of the user\
     and percentage after user successfully logs in'''
     #total questions is the no of question in csv we have
    
    mydb=mysql.connect(username="root",passwd=pass_sql,host="localhost",database="codecs")
    mycur=mydb.cursor()
    mycur.execute(("select username from users where uid='{}'").format(uid))
    username=mycur.fetchall()[0][0]
    print(("WELCOME {}".center(50,'=')).format(username))
    mycur.execute(("select count(*) from {} where status=1").format(uid))##fetching all the records with status 1
    data=mycur.fetchall()
    #countDone stores no of 1's that is status - completed
    countDone=data[0][0]##data is a list of tuple having the count
    
    prgPer=(countDone/totalQues)*100##calculating the progress percent of user
    var='■'
    print("Your Current Progress Bar :")
    ##printing the progress bar
    for i in range(1,round(prgPer)+1):#rounded off to nearest integer
        time.sleep(0.05)
        print('\r', str(i) +'% Completed',end='')#printing percentage each time
        print('\r',var*i,end='')#printing the square block
    print('->'+str(round(prgPer))+"% Completed")#printing in end the bar

    #displaying star level and levels (ABC)
    print("level : ",end = ' ')
    
    minimum=totalQues//3
    if 0<countDone<=minimum:#checking if user is A level
        print("A")
        print("Star Level: *")
        #return 'A'#returning A so that user can get A level questions
    elif minimum<countDone<=minimum*2:#checkingfor Blevel
        print("B")
        print("Star Level: * *")
        #return 'B'#returning B so that user can can get B level
    elif minimum*2<countDone<=minimum*3:
        print("C")
        print("Star Level: * * *")
        #return 'C'

    else:
        print("You have not got any level yet")
        print("Successfully complete your first question now")
        #return 'A'# since user hasn't progressed yet, thus A level questions will be displayed
    cont=input("PRESS ENTER TO GO BACK".center(60,'='))
    os.system('cls')
    MAL.afterLog(pass_sql,uid)
