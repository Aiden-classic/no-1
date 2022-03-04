import os
# kol qesmt ha dr in brname hst
message="Babak Khorramdin"
while True:
    a=input("select ")
    if a=="1":
        print(message[0])
        input("press any key ")
        os.system('clear')
    if a=="2":
        print(message[6])
        input("press any key ")
        os.system('clear')
    if a=="3":
        m1="Babak"
        m2="Khorramdin"
        for i in range(len(message)):
            if message[i]==m1[0]:
                flag=True
                for j in range(len(m1)):
                    if(message[i+j]!=m1[j]):
                        flag=False
        if flag==True:
            print(m1)
        for i in range(len(message)):
            if message[i]==m2[0]:
                flag=True
                for j in range(len(m1)):
                    if(message[i+j]!=m2[j]):
                        flag=False
        if flag==True:
            print(m2)
    if a=="4":
        for i in range(0,12,2):
            print(message[i])         
    if a=="5":
        msg="false"
        for i in message:
            if i=="m":
                msg="true"
                break
        print(msg)          



       
