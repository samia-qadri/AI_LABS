# LAB EX 01: (i) 

height = float(input("Enter height in cm : "))
width=float(input("Enter width in cm : "))
depth=float(input("Enter depth in cm : "))
volume= height*width *depth

print("\nVolume of object: ",volume)

if(volume <1):
    print("Label : Invalid inputs.")
elif (volume <= 10):
    print("Label : extra small")
elif (volume <= 25):
    print("Label : small")
elif (volume <= 75):
    print("Label : Medium")
elif (volume <= 100):
    print("Label : Large")
elif (volume <= 250):
    print("Label : Extra Large")  
else :
    print("Label : Extra Extra Large")  
    
    
# ii
worker_time = float(input("Enter time taken by worker : (in hours)  "))
if worker_time <0:
    print("Invalid input")
elif( worker_time <= 3):
    print("Highly efficient")
elif( worker_time <= 4):
    print("Improve your speed")
elif( worker_time <= 5):
    print("Take the training to improve speed")
else:
    print("You may leave the company ! ")

# iii 
username= input("Enter your username : ")
password = input("what is the password ? ")
real_password= "abc$123"

if(password.lower() == real_password): #as in question->password not case sensitive
    print("Welcome ! ")
else:
    print("I don't know you. ")
    
    
# EXERCISE 2 -> OUTPUT QUESTIONS
n = 3 
while n >= 0: 
    n -= 1 
    print(n) 
    
'''1. Create a loop that counts from 0 to 100 
2. Make a multiplication table using a loop 
3. Output the numbers 1 to 10 backwards using a loop
4. Create a loop that counts all even numbers to 10 
5. Create a loop that sums the numbers from 100 to 200 
'''
# 1  Create a loop that counts from 0 to 100 

for n in range(101):
    print(n)
    #n+=1
    
# 2. Make a multiplication table using a loop
num=int(input("Enter number whose table you want : "))
# n=1
for n in range(1,11):
    print(num ," * ",n," = " ,num*n)
    

# 3. Output the numbers 1 to 10 backwards using a loop
n=10
while(n>0):
    print(n)
    n-=1

# 4. even number count to 10
count=0
print("even numbers are as: ")
for i in range(0,11):
    if(i% 2==0):
        count+=1
        print(i)
print("total even numbers are : ",count)

# sums number from 100 to 200
sum=0
for i in range(100,201):
    sum +=i
print("Sum of numbers between 100 to 200 is : ",sum)

# 
clist = ["Canada","USA","Mexico"]
i = 0
while i< len(clist):
    print(clist[i])
    i +=1
    
    
    
