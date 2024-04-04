def updProgress(sqlp,uid,qid,timeTaken):
    import UserLevel as UL
    import mysql.connector as mysql
    import CodeEnv as CE
    from os import remove
    mydb=mysql.connect(host='localhost',user='root',password=sqlp,database='codecs')
    mycur=mydb.cursor()
    #CE.codeInputInterface('LA1')
    p=CE.codeOutputInterface(qid,timeTaken)
    remove(qid+'.py')##removing file after use for memory management
    m=p[1]
    if p[0]=='testSuccess':
        mycur.execute('update {} set status=1,memory="{}" where qid="{}";'.format(uid,m,qid))
    else:
        return 'failedCase'
        #mycur.execute('insert into {} values("",0,"{}");'.format(uid,m)) 
    mydb.commit()
    
def quesMenu(sqlp,uid):
    import os,csv,time
    import UserLevel as UL
    import mysql.connector as mysql
    import CodeEnv as CE
    mydb=mysql.connect(host='localhost',user='root',password=sqlp,database='codecs')
    mycur=mydb.cursor()
    #sqlp='tiger'
    print("Redirecting to the question page...")
    time.sleep(1)
    os.system('cls')
    print("======================Question page=======================")
    f=open("Ques.csv","r",newline="")
    r=csv.reader(f)
    next(r)
    print("List of the ids of the questions:")
    level=UL.userLevel(sqlp,uid,15)
    print("Level: ",level)
    q="select qid from {0} where status=0 and qid like '%{1}%';".format(uid,level)
    #print(q)
    
    notattqid_obj=mycur.execute(q)
    #notattqid=not attempted ques id
    notattqid=mycur.fetchall()
    #print(notattqid)
    #if notattqid!=None:
        #print(notattqid)
    #print the questions of a particular level
    for i in r:
        if  (i[0],) in notattqid:
            print(i[0])
        
    f.seek(0)
    qid=input("Enter one of the given question ids to attempt the desired question:").upper()
    for j in r:
        if j[0]==qid and (j[0],) in notattqid:
            os.system('cls')
            print("Question:",j[1],'\n','Given Value:',j[2],'\n',"Begin whenever ready\n")
            timeTaken=CE.codeInputInterface(qid)
            os.system('cls')
            updProgress(sqlp,uid,qid,timeTaken)
        else:
            continue

