# # pratice set number 01 sum of two numbe:

a = int(input("Enter 1st digit: "))
b = int(input("enter 2nd digit: "))
print("sum of the number is: ", a + b)

# pratice question number 02 find remender using modules opratior:

a = float(input("enter number: "))
b = float(input("enter 2nd number: "))
c = a % b
print("remender off the number is: ", c)
# pratice question 03 typecasting

a = input("enter the value you wnat's to see thear type: ")

print(type(a))

# question 04 find greatest number in two variables

a = int(input("Enter the first value: "))
b = int(input("Enter the 2nd value: "))
print(a, "is greater then ", b, "is: ", a > b)

# question 5 finnd the avrage of the number:
a = int(input("enter the 1st number: "))
b = int(input("enter the 2nd number: "))
print("avrage of  the number is:  ", (a + b) / 2)

# question 06 Find the square of the number:

a = int(input("enter the value: "))
print("square of the number is: ", a * a)

#  printing real + imaginary numbers:
cn = complex(2, 5)
print("ENter number: ", cn)
print("Complex - real part: ", cn.real)
print("Complex - imaginary part: ", cn.imag)

# adding two complex number:


a = complex(10 + 2j)
print(a)

# printing complex number but taking input from user:
a = complex(input("Enter the 1st number: "))
b = complex(input("Enter the 2nd number: "))
print("sum of the complex number: ", a + b)
print("Complex - real part: ", a.real)
print("Complex - imaginary part: ", b.imag)
