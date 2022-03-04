import math
import os
while True:
    a=input("enter ")
    if a=="exit":
        break
    a=float(a)
    print("V=",(4/3)*math.pi*a**3)
    input("press any key")
    os.system('clear')

