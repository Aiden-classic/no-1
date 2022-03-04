qq=1
for  i in range(10):
    for j in range(10):
        if((j+1)*qq<10):
            print((j+1)*qq,end="   ")
        else:
            print((j+1)*qq,end="  ")

    qq+=1
    print(" ")    
