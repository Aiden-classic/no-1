from cmath import pi
import os
a=int(input("pls enter arz "))
b=int(input("pls enter tool "))
qq=a
for i in range(a):
    print("  "*qq,end="")
    for j in range(b):
        if(i==0 or i==a-1):
            print("* ",end="")
        else:
            if(j==0 or j==b-1):
                print("* ",end="")   
            else:
                print("  ",end="")    
    print("")
    qq-=1