a=int(input("pls enter number 1 "))
b=int(input("pls enter number 2 "))
c=int(input("pls enter number 3 "))
qq=list()
qq.append(a)
qq.append(b)
qq.append(c) 
max=a
min=a
for i in qq:
    if(i>max):
        max=i
    if(i<min):
        min=i
print("max = ",max)
print("min = ",min)