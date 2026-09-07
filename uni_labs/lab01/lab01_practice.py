print(1+2+3)
print(1==0)
print("Artificial"+" Intelligence")
print("software engineering".upper())
print("software engineering".title())
print(len("software engineering"))

num = 8.0
num+=1.45
print(num)

print("BUILT IN DATA TYPES ")
# === LIST ===
print("List : ")
fruits = ['apple','banana','mango']
print(len(fruits))
other_fruits= ['kiwi','orange','grapes','pear']
fruits+=other_fruits
print(fruits)
print(len(fruits))
print("fruit at index -2 is : ",fruits[-2])
pop_element = fruits.pop()
print("element poped is : ",pop_element,"and other are as : ",fruits)

#slicing 
print(fruits[2:-2])

list_02=[[1,2,3],['one','two','three'],['a','b','c','d']]
print(list_02[1][2])

print(list_02)
list_02[2].pop()
print(list_02)

# === TUPLES === ( immutable )
pair= (3,5)
print(pair[0])
x,y = pair
print("value of x is  : ",x," and y is : ",y)
# print(pair[0] = 5) # error  - not allowed

x = 6 
if (type(x) is int):  
    print("true")  
else:  
    print ("false") 
    
x = 7.2 
if (type(x) is not int):  
    print ("true")  
else:  
    print ("false") 
    

list1=[1,2,3,4,5]  
list2=[6,7,8,9]  
for item in list1:  
    if item in list2:  
        print("overlapping")      
else:  
    print("not overlapping") 
    
a//=3 # error a not defined
a**=5 
print("floor divide=",a) 
print("exponent=",a) 


a = 60
b = 13
c = 0

c = a & b #bitwise AND      #first convert into binary then operations perform hongy
print("Line 1", c)
c = a | b           # a and b my OR operator krky ans ay wo
print("Line 2", c) 
c = a ^ b           # xor  # same bits → 0 Different bits → 1
print("Line 3", c)
c = ~a              #not
print("Line 4", c)
c = a << 2          #left shift =>bits ko 2 positions left shift karna.
print("Line 5", c)
c = a >> 2          #rightshift =>bits ko 2 positions right shift karna.
print("Line 6", c)
