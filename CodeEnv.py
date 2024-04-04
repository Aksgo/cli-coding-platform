import time
import os
import sys
import csv
#import compiler
#save command = 'cmdsave'
cwd=os.getcwd()
dirc=cwd+"\\Ques.csv"
def codeInputInterface(qid):
    '''this function takes the input of the code from the terminal window \
    after user selects a particular problem using qid'''
    qfile=qid+'.py'
    
    #print("#for an input program please specify your input variable as '=datatype(inputParam)'")
    print("#Return the final answer using return")
    print("#Type command - 'cmdsave' to end input to stdin\
    \n#NOTE:Once a single line is typed and entered you cannot revert back\
    \n#In case if you want to type again - type 'reset' and start again from next line")
    print('1.',end=' ')
    print("def {}():".format(qid))
    print("\t#write your code below")

    codeFile=open(qfile,'w')#taking input of code and apppending it to file  with name qid.py
    
    data = ['def userInput(inputParam=None):\n']
    stime=time.perf_counter()
    i=2
    while True:
        print(str(i)+'.',end=' ')
        #The perf_counter() function always returns the float value of time in seconds.
        line=input()
        endcmd=line[-7:].lower()
        if endcmd!='cmdsave':
            if endcmd=='reset':
                i=2
                print('1.',end=' ')
                data = ['def userInput(inputParam=None):\n']
                print("def {}():".format(qid))
                print("\t#write your code below")
                continue
            else:
                i+=1
                #line='\t'+line
                line+='\n'
                data.append(line)
        
        else:
            etime=time.perf_counter()
            b=etime-stime
            #print("--> Time Taken : ",b,'seconds')
            break
        
    flag=0
    ##checking if no input is given
    for i in range(1,len(data)):##checking for empty statements
        line=data[i]
        if line[1:-1] not in ' '*len(line):#checking for at least any statement given
            flag=1
            break
        else: 
            flag=0
    if flag==1:#means a statement found
        codeFile.writelines(data)
    else:#flag=0 means no code given
        data=['def userInput(inputParam=None):\n','\tpass']
        codeFile.writelines(data)
    
    codeFile.close()##closing qid.py file
    return b
    ##code to be designed - counting errors
    '''countError=compiler.codeErrorCounter(data,qid)##passing code data and qid to check for input parameter
    
    print(countError)
    # check if file exists
    if os.path.exists("Temporary.py"):
        os.remove("Temporary.py")##deleting the file after checking all the error counts
    '''
#codeInputInterface('LA1')

def codeOutputInterface(qid,timeTaken):
    '''this function is to print the output of userInput()
       that is code given by user'''
    import importlib#importing to change file name in string as a module
    try:
        qidModule=importlib.import_module(qid)#converted to module
    except Exception as e:#indentation error in main file
        print('COMPILATION ERROR :('.center(50,'-'))
        print('->',e)##returns the indentation error
        print("Test Case Failed".center(50,'='))
        return 'OutputRunFailed',0
        
        
    '''
    importlib.reload(module)->
    reloading the module of user input so that new output is returned to stdout
    '''
    importlib.reload(qidModule)
        
    try:#trying incase any error in user input
        
        #print(qidModule)
        quesFile=open('Ques.csv','r',newline='')#accessing csv file of question to display selected ques
        reader=csv.reader(quesFile)
        
        for i in reader:
            if i[0]==qid:

                inputParam=i[2]##i[2] is the custom input
                reqOutput=i[3]# our requird output
                break
            else:
                continue

        print('GIVEN INPUT'.center(50,'='))
        print(inputParam)
        print('UNEXPECTED PRINT STATEMENTS'.center(50,'-'))#unexpected print statements in user input ignored
        timeInitial=time.perf_counter()
        data=qidModule.userInput(i[2])#storing the return value in variable data
        timeFinal=time.perf_counter()
        print("None")##for unexpected statements (either given or not)
        print('EXPECTED OUTPUT'.center(50,'='))
        print(reqOutput)
        
        print('YOUR OUTPUT'.center(50,'='))
        print(data)#printing the output to terminal
        quesFile.close()
        memoryTaken=os.path.getsize(qid+'.py')
        print("--> Memory Usage : ",memoryTaken,'bytes')
        print("-->Execution time : ",timeFinal-timeInitial,"seconds")
        print("-->Typing Time Taken : ",round(timeTaken,2),'seconds')
        
        if str(data)==reqOutput:#checking id output is correct
            #type conversion becuase req op is string
            ###successs animation to be given
    
            print("Test Case Successful".center(50,'='))
            return 'testSuccess',memoryTaken
        else:
            print("Test Case Failed".center(50,'='))
            return 'testFailed',memoryTaken
        
    except Exception as e:#either input error or file error
        print(None)
        print('COMPILATION ERROR :('.center(50,'-'))
        print('->',e)
        print("Test Case Failed".center(50,'='))
        return 'OutputRunFailed',0
    

#codeOutputInterface('LA1')

