def encrypt(list1):
    keys={"!":10,"@":20,"#":30,"$":40,"%":50,"^":60,"&":70,"*":80}
    enkeys=[]
    enlist=[]
    enlist2=[]
    enlist3=[]
    from random import choice as ce
    for i in list1:
        l1=[]
        for j in range(len(i)):
            l1.append(ord(i[j]))
        enlist.append(l1)
    #print(enlist)
    for i in enlist:
        l2=[]
        k1=ce(["!","@","#","$","%","^","&","*"])
        enkeys.append(keys[k1])
        for j in range(len(i)):
            i[j]+=keys[k1]
            l2.append(i[j])
        enlist2.append(l2)
    #print(enlist2)
    #print(enkeys)
    for i in enlist2:
        st1=''
        for j in range(len(i)):
            st1+=(chr(i[j]))
        enlist3.append(st1)
    list1=enlist3
    #print(list1)
    return list1,enkeys

def decrypt(list1,enkeys):
    de1=[]
    de2=[]
    de3=[]
    for i in list1:
        l4=[]
        for j in range(len(i)):
            l4.append(ord(i[j]))
        de1.append(l4)
    #print(de1)
    dy=0
    for i in de1:
        l5=[]
        for j in range(len(i)):
            i[j]-=enkeys[dy]
            l5.append(i[j])
        de2.append(l5)
        dy+=1
    #print(de2)
    for i in de2:
        st=""
        for j in range(len(i)):
            (st)+=(str(chr(i[j])))
        de3.append(st)
    #print(de3)
    list1=de3
    return list1
'''
data,key=encrypt(['hello'])
print(data)
print(key)
data2=decrypt(data,key)
print(data2)
'''
