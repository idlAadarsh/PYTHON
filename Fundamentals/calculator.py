no1=int(input("1st no."))
no2=int(input("2nd no."))
cal=int(input("(NOTE: 1 for +, 2 for -, 3 for *, 4 for /)your response :"))
if cal==1:
    a=no1+no2
    print(a)
elif cal==2:
    b=no1-no2
    print(b)
elif cal==3:
    c=no1*no2
    print(c)
elif cal==4:
    d=no1/no2
    print(d)
else:
    print("please choose correct combination")