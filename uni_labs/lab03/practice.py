#normal function: 
def add10(a):
    a=a+10
    print(a)   
a=3
add10(a)

#lambda function 
x= lambda a: a+10
ans=x(2)
print(ans)

x= lambda a,b : a*b
print(x(2,3))

x=lambda a,b,c : a+b+c
print(x(2,3,5))

# ARRAY
colours= ['red','blue','yellow'] # actually a list , we use it as array rn
print(colours[0])
colours[2]='black'
print(colours)

print(len(colours))
i=1
for colour in colours:
    print(i,"- ",colour)
    i+=1
    
# EXERCISE QUESTIONS OF ARRAY AND LAMBDA

# EXERCISE 01
# === i ===
sq = lambda a: a*a
cube= lambda x : x*x*x

numbers= [1,2,3,4,5]
for n in numbers:
    print("Number : ",n," it's square : ", sq(n), " and cube : ",cube(n))

# === ii ===
ans= lambda string,char : "yes" if string[0].lower() ==char.lower() else "no"
print(ans("Software","s"))


# ==== iii ====
# to import date year import an library
from datetime import datetime

year= lambda x: x.year
month= lambda x: x.month
date= lambda x: x.day
time= lambda x: x.time()

d= datetime.now() #for today's date

print("Year : ",year(d))
print("Month : ",month(d))
print("Date : ",date(d))
print("Time : ",time(d))


# for manual input 
# d= input("Enter year, Month, Date, Time in format YYYY-MM-DD-Hour : ")
# d= datetime.strptime(d, "%Y-%m-%d-%H") # format define krdia