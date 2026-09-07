f= open("cities.txt","w")

n =int (input("Enter how many cities you want to add : "))
for i in range(n):
    print(" For ",i+1," city : ")
    name= input("Name : ")
    population= input("Population : ")
    mayor= input("Mayor :  ")
    f.write(f"{name}  ,{population},  {mayor} \n")

print("Added successfully ! ")
f.close()
f_r = open("cities.txt","r")
f_r.read()
f_r.close()

#  II - student.txt
 # method to write + read => w+
with open ("student.txt","w+") as f:
    f.write("We are 4th sem students. ")
    data= f.read()
    print(data) 
    
   # OR 2nd method
f = open("student.txt","a")
f.write("Now we are AI students")
f.close()
f_r = open("student.txt","r")
print(f_r.read())
f_r.close()