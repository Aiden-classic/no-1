import random
flag=0
a=random.randint(1,20)
for i in range(5):
    num=int(input("pls enter a number "))
    if num==a:
        print("Good job number was ",a)
        flag=1

if flag==0:
    print ("number was ",a)        