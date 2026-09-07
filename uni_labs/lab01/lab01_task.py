s="hello world"
print(dir(s))

help(s.find) # displays  documentation for find method

#other string fucntion
str = 'artificial Intelligence'
print(str.upper())
print(str.lower())
print(str.title())
print(str.find('cial')) #returns starting index of occurence

print (str.count('i'))
print("Is Alphabetic:",str.isalpha())
print("Is Alphanumeric:",str.isalnum())
print("Is numeric" ,str.isnumeric())
print("Split:", str.split())


#Before swapping 
a=2,b=56,c=78,d=9 
#After Swapping 
#a=,9,b=78,c=56,d=2 

a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
d=int(input("Enter value of d: "))

print(" Before Swapping : ")
print("a :", a, ",b :", b, ",c :", c, ",d :", d)
a, b, c, d = d, c, b, a
print(" After Swapping ")
print("a :", a, ",b :", b, ",c :", c, ",d :", d)


'''Write a Python program to convert temperatures to and from celsius, 
Fahrenheit. 
Formula : c/5 = f-32/9 
Expected Output : 
Enter temp in Celsius: 60°C 
Temperature in Fahrenheit is :140ss '''

temp_c = int(input("Enter temperature in celsius : "))
temp_f= ( ( temp_c / 5 ) *9 ) +32
print("temp in fahrenheit is : ",temp_f)

# list
colours= ['red','green','yellow','blue']
other_colours= ['purple','pink','white','black','lavendar']
list_colours= colours + other_colours

print("length of list is : ",len(list_colours))
list_colours.insert(5, 'brown')
print("length of list is : ",len(list_colours))
list_colours.pop()

nums= [ 99, 2,13,0,4,86,68 ]
nums.sort()
print("sorted list :", nums)
nums.reverse()
print("reverse list :", nums)

''' (ii)Write a Python program to count the number of strings where the string length is 2 or more and the 
first and last character are same from a given list of strings.  
Sample List : ['abc', 'xyz', 'aba', '1221'] 
Expected Result : 2.  '''

str_list = ['abc', 'xyz', 'aba', '1221']

count = 0
for element in str_list:
    if ((len(element)>=2) and element[0] == element[-1]):
        count+=1
print("Result:", count)

# DICTIONARY
print(dir(dict))
print("\nFUNCTION OF from keys function:")
help(dict.fromkeys) 

# concatenate into new one 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
newdict= dic1.copy()
newdict.update(dic2)
newdict.update(dic3)

print(newdict)

''' Write a list comprehension which, from a list, generates a lowercased version of each string that has 
length greater than five.   '''
org_list= ['BSSE','university of Karachi','data science', 'UBIT', 'Karachi','NIVIDIA']
new_list_lower=[]
for element in org_list:
    if(len(element)>5):
        new_list_lower.append(element.lower())
    
print(new_list_lower)

'''(ii)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements  
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink'] 
Expected Output : ['Green', 'White', 'Black'] '''
colours_list= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink'] 
del colours_list[5]
del colours_list[4]
del colours_list[0]
print(colours_list)




