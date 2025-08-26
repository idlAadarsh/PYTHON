"""for i in range(1,101):
    if i%2==0:
        p=i*2
        print(p)"""
"""k=0
sum of 1 to 10
for i in range(1,11):
    print(i)
    k+=i
print(k)"""
"""multiply of input no."""
"""a=int(input("no."))
for i in range(1,11):
    b=a*i
    print(a,"*",i,"=",b)"""
#reversed counting
"""i=int(input("no."))
for i in range(i,0,-1):
    a=i
    a*=i
    print(a)

assignment operator

a=int(input("1st siide"))
b=int(input("2nd siide"))
c=int(input("3rd siide"))
if a==b and b==c and a==c:
    print("equilateral triangle")
elif a==b or b==c or a==c:
    print("isosceles triangle")
else:
    print("scalene")"""

"""continue=skiip break=stop"""

"""
a=int(input("enter the nubmer"))
flag=0
for i in range(2,a):
    if a%i==0:
        flage==1
        break
if flage==1:
    print("not prime ")
else:
    print("print")
"""

"""digit reverse no"""

# a=int(input("enter the number"))
# rev=0
# while a>0:
#     b=a%10
#     rev=rev*10+b
#     a=a//10
# print("reserse of ",rev)
# #  digit count
# # digiit sum

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# k=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(2*i-1,end=" ")
#     print()

# k=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()
# # not completed
# for i in range(6,1,-1):
#     for j in range(i):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(6,i+1,-1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()



# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range():

#pattern 


# for i in range(1,6):
#     k=65
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()


# k=65
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()

#backward indexing in python

#l1=[1,2,3,4,5,6,7,8,9,10]
# print(l1[-3])
# print(l1[3])

# traversing: dishplay the element data one by one 
# some of list data (a=0,for adding the numbers )
#printing even numbers from list by using mouduler

# a=0
# for i in l1:
#     if i%2==0:
#        print(i)

#traversing in range 

# a=len(l1)
# for i in range (0,a): #in bracket used (0,a) 0 is used for indexing 
#     print(l1[i])  #imp l1[i]

 
# li=[10,13,40,43,53]
# for i in range()

# HOW TO TAKE LIST FROM THE USER  AND ADD EVERY NUMBER IN FROM THE LIST 

# l1 = eval(input('enter the element'))
# a=len(l1)
# sum=0
# for i in l1:
#     sum+=i
# print(sum)

# EVEN NUMBER PRINTING FROM LIST DATA 

# l1=eval(input("enter the element"))
# for i in l1:
#     if i%2==0:
#         print(i)

#checking number are available in list or not 

# l1=eval(input('enter the number'))
# num=list(input('enter the num'))
# for i in l1:
#     if (num in i):
#         print('this number found in list')
#     else:
#         print('not found')

#slicing :- creating a sub list from exciting list
# la=[1,2,3,4,5,6,7,8,9]
# print (la[2:7])
# print(la[1:7])
# print(la[-2:-8:-1])

# list manipulation
#append: 1adding new elements in list append

# la.append(6)
# print(la)

# update the element

# la[1]=5
# print(la)

# delete del keyword
# la=[1,2,3,4,5]
# del la[2]
# print(la)

# del la[1:4]
# print(la)

# list function /method

# index() it return the index of the given value

# la=[1,2,3,4,5,6,7,8]
# print(la.index[2.5])

# reverse()
# la=[1,2,3,4,5]
# # la.reverse()
# # print(la)
# # clean
# la.clear()
# print(la)
# count

# linear search

# l1=eval(input('enter the number'))
# num=int(input('enter the num'))
# flag=0
# for i in l1:
#     if num ==i:
#         flag=1
#         break
# if flag==1:
#     print('this number found in list')
# else:
#     print('not found')

# TOUPLES: COLLEtions of different type of data within()
# ta=(1,2,3,4,5)
# print(ta[4])

# traversing in tuple

# la=tuple(input("enter the number"))
# for i in la:
#    print(i)

# # traversing with range in tuple

# l1=(1,2,3,4,5)
# a=len(l1)
# for i in range (a):
#     print(l1[i])

# TRAVERSING IN DICTIONARY

# d1={
#     'name':'aadarsh kumar',
#     'roll no':'1234',
#     'add.':'home- 43, '
# }
# for i in d1:
#     print(i,':',d1[i])

# ADDING KEY VALUE AND UPDATING IT WITH SAME SYNTEX

# d1['subject']='english'
# d1['roll no']='2345'
# print(d1)

# MAKING PROCESS OF DICTIONARY FROM USER
# d={}
# num=int(input("enter the total key value pair"))
# for i in range (1,num+1):
#     key=input("enter the key")
#     value=input("enter the value")
#     d[key]=value
# print(d)

# STRING
# s1='hello world'
# print(s1[2:6]+s1[7:10])
# print(s1[11:15])

