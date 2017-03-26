x = 'Md Shakib Hassan'
y= '01*2**0**52'
print('Name :',x)
print('Mobile No.: ',y)
a = round(float(input("Enter You'r number: ")))
if a>=80 and a<=100:
    print('A+')
elif a>=70 and a<=79:
    print('A')
elif a>=60 and a<=69:
    print('A-')
elif a>=50 and a<=59:
    print('B')
elif a>=40 and a<=49:
    print('C')
elif a>=33 and a<=39:
    print('D')
elif a>=0 and a<=32:
    print('F')
else:
    print('''Your number is invalid.
Please,try to enter between 0 to 100
****** Thank You  ***** ''')
    
