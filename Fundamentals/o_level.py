# This code converts temperatures between Fahrenheit and Celsius.

fohr = int(input('enter fohrenheit'))
cel = (fohr-32)*5/9 # (fohr-32)/1.8
print(cel)

cell = int(input('enter celsius'))
forh = cell*9/5+32 # cell*1.8+32
print(forh)

# This code checks if a number is even or odd.

num= int(input("enter the num"))

if num%2==0:
    print('this number is even')
else:
    print('this number is odd')

# area and cercumfrance of circle

import math
radius = float(input('enter radius'))
area =  math.pi*radius**2
cercum= 2*math.pi*radius

print(f"area is {area} cercumfrance is {cercum}") # this is a formatted string literal (f-string) for better readability
# syntex of f-string: f"string{value:.formatting} where .formatting is optional or can be used to format the value

# this codes check character is vowel or not

char= input('enter any char')
if char== "a" or char == "A" or char== "e" or char=="E" or char =="i" or char== "I" or char== "i" or char == "O" or char== "o" or char == "U" or char == "u":
    print (f"{char} is vovel")
else:
    print(f"{char} is not vovel")

# same code but using in operator for better readability

CHAR = input("enter any char: ")
vovel= ["a","A","e","E","i","I", "o","O","U","u"]
if CHAR in vovel:
    print(f"{CHAR} is vovel")
else:
    print(f"{CHAR} is not vovel")

# lets check number is positive, negetive or zero

Num = int(input('enter any number'))
if Num>0:
    print(f"{Num} is positive")
elif Num<0:
    print(f"{Num} is negetive")
else:
    print(f"{Num} is zero")

# lets check given integer is a multiple of 5 or not

n = int(input('enter any number'))
if n%5==0:
    print("it is multiple of 5 ")
else :
    print('it is not a multiple of 5')

#grade system between 0.0 to 1.0

g=float(input('enter the num'))
if g>1.0 or g<0.0:
    print('error')
elif g>=0.9 and g<=1.0:
    print("Grade A")
elif g>=0.8 and g<0.9:
    print("Grade B")
elif g>=0.7 and g<0.8:
    print("Grade c")
elif g>=0.6 and g<0.7:
    print("Grade D")
elif g>=0.5 and g<0.6:
    print("Grade E")
else:
    print("Fail")
# better for readability using elif
g = float(input('Enter the number: '))

if g > 1.0 or g < 0.0:
    print('Error')
elif g >= 0.9:
    print("Grade A")
elif g >= 0.8:
    print("Grade B")
elif g >= 0.7:
    print("Grade C")
elif g >= 0.6:
    print("Grade D")
elif g >= 0.5:
    print("Grade E")
else:
    print("Fail")

# successor and predecessor of largest number in a list

mylist = []
tn=int(input('enter how much number would be in list'))
for i in range(0,tn):
    num=int(input('enter list num'))
    mylist.append(num)
mylist.sort() # instead of sorting, we can also use max() to find the largest number
print(mylist[-1]+1) # successor of largest number
print(mylist[-1]-1) # predecessor of largest number
print(mylist)

# showing odd, even and zeros from a list 
list=[]
tItems=int(input("enter the num which should be in list"))
for i in range(0,tItems):
    items=int(input("enter the nums"))
    list.append(items)
print(list)
tEven=0
tOdd= 0
zeros=0
for i in list:
    if i==0:
        zeros+1
    elif i%2==0:
        tEven+=1
    else:
        tOdd+=1
print(f"total even nums are {tEven} total odd nums are {tOdd} and zeros are {zeros}")
        

# input list from the user and give him in output largest value, smallest value and product of all numbers in the list
import math
itemsNum=int(input('enter the number of list items'))
numList = [int(input('enter the number:'))for i in range(itemsNum)]
print(f"the largest number in the list is {max(numList)} and the smallest number in the list is {min(numList)} and product is {math.prod(numList)}")


# factorial of a number
num = int(input("enter the num"))
fact= 1
if num<0:
    print('this is for positive numbers')
    
else:
    for i in range(1,num+1):
          fact*=i
print(fact)

# same thing using while loop 
while True:
    num = int(input("Enter a positive number: "))

    if num < 0:
        print("❌ Negative numbers are not allowed. Try again.")
    else:
        break   # valid number → exit loop

fact = 1
for i in range(1, num + 1):
    fact *= i

print(f"✅ Factorial of {num} is {fact}")

# finding largest positive number, smallest negative number and sum of all positive numbers in a list
num = int(input("enter the number: "))
arr= [int(input("enter the number: ")) for i in range(num)]
sum= 0
for i in arr:
    if i>0:
        sum=i+sum
print(f"largest positive number in the list: {max(arr)} the smallest number: {min(arr)} and sum of all positive number is: {sum}")
print(arr)

# removing items from a list using pop method
num = int(input("enter the number: "))
myList = [int(input("enter the list item: ")) for i in range(num)]
iValue = int(input("enter index value: "))

myList.pop(iValue)
print(myList)

# sum of all odd numbers till nth number:
num = int(input("enter ending number"))
oddSum = 0
for i in range(num+1):
    if i%2!=0:
        oddSum+=i
        print(oddSum)

print(oddSum)

# sum of 3 numbers using list comprehension
nums =[ int(input(f"Enter number{i+1}: ")) for i in range(3)]
print(f"total of 3 number is :{sum(nums)}")

# square root of 3 numbers and also their sum using list comprehension
import math
root = [int(input(f"Enter {i+1} squareroot: ")) for i in range(3)]
print(f"squareroot of {root[0]} is {math.sqrt(root[0])},squareroot of {root[1]} is {math.sqrt(root[1])} and squareroot of {root[2]} is {math.sqrt(root[2])} and sum of all squareroot is {math.sqrt(root[0])+math.sqrt(root[1])+math.sqrt(root[2])}")

# checking if an integer is available in a list or not and add it if not available
Mylist = [int(input("enter List items: ")) for i in range(5)]
item= int(input("number for checking in list: "))
if item in Mylist:
    print('yeah item integer is available in list')
else:
    print('no item is not available and adding that number')
    Mylist.append(item)
    print(f"added,{Mylist}")

#  dictionary operations: adding, updating and printing
dictionary= {
    "name": "aadarsh kumar",
    "Roll":19
}
dictionary.update({"subject":"english"})
dictionary["marks"]="85%" #this is another style of adding or updating dictionary
print(dictionary)

#   multiplication of two numbers using repeated addition
# This code takes two integers as input and calculates their product using repeated addition.
a= int(input("enter the number: "))
b= int(input("enter second num: "))
result= a*b
expression= '+'.join([str(a)]*b)

print(f"{a}*{b}={expression}={result} ")

# sum of all numbers till nth number
num= int(input("enter number for sum: "))
sum= 0
for i in range(num+1):
    sum+=i
print(sum)

# sum of all digits in a number
num= input('enter numbers')
sum= 0
for i in num:
    sum+=int(i)
print(sum)