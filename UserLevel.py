import mysql.connector as mysql
import time
def userLevel(sqlp,uid,totalQues):
    '''this function returns the level of the user with a specific uid'''
    mydb=mysql.connect(username="root",passwd=sqlp,host="localhost",database="codecs")
    mycur=mydb.cursor()
    mycur.execute(("select count(*) from {} where status=1").format(uid))##fetching all the records with status 1
    data=mycur.fetchall()
    countDone=data[0][0]##data is a list of tuple having the count
    minimum=totalQues//3
    if 0<=countDone<minimum:#checking if user is A levl
        return 'A'#returning A so that user can get A level questions
    elif minimum<=countDone<minimum*2:#checkingfor Blevel
        return 'B'#returning B so that user can can get B level
    elif minimum*2<=countDone<=minimum*3:
        return 'C'
    else:
        print("----Level Error----")

