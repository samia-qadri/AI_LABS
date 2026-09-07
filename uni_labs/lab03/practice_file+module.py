f= open("demofile.txt","w") # w is liye likha taky file agr nhi hy to create hojay.
f=open("demofile.txt","a")
f.write("Hello ! This is line No. 01")
f.close()

# reading the file
f=open("demofile.txt","r")
print(f.read())
f.close()

f=open("demofile.txt","w")
f.write("OOps ! I've deleted the content")
f.close()

f=open("demofile.txt","r")
print(f.read())
f.close()

# practice module
import mymodule
mymodule.greeting("samia")

a= mymodule.person1["age"]
print(a)

import math as maths
print(maths.sqrt(25))

from math import sqrt as squareroot
print(squareroot(9))

import time as t
s= t.time()
print(s)

print(t.ctime(s))

print("Start")
t.sleep(3)
print("End")

# glob library file ka pattern maths kry gi like glob.glob("pattern")
import glob as g
print(g.glob("*.py")) #tamam py files ky name ajay  gy
print()
print(g.glob("*"))
print("")
# for ex mujhe student ky name wali file chhaiye
print(g.glob("student*.txt"))


import random

x=[1, 2, 3, 4, 5]
random.shuffle(x) # original list my hi changes krdy ga
print(x,2) 

print(random.randint(1,80))
print(x)