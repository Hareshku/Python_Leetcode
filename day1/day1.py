# # variable is name of memory location in program or container to store the data
# name ="Haresh"
# rollNo="21SW053"
# department="Software Engineering"

# print("name =",name, "\nrollNo =",rollNo, "\ndepartment =", department)


# # data types and input output 
name= input("Enter your name =")
age= int(input("Enter you age  ="))

# print("Name =",name, "\nage =", age)

# Using f-string (most modern & clean)
print(f"Hello {name}, you are {age} years old!")

# Using str.format()
print("Hello {}, you are {} years old!".format(name, age))

# Using % formatting (older style)
print("Hello %s, you are %d years old!" % (name, age))

b=False
x="100"
y=int(x)
z= float(x)
print(y+2, z+3, b)

print("Arthmatic")
a, b= 10, 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a//b)
print(a%b)
print(a**b)

print("comparison")
print(a==b)
print(a!=b)
print(a>b)

print("Logical operators")
x, y= True, False

print(x and y)
print(x or y)
print(not x)


print("assignment")
a= 4
a +=2
a-=1
a*=3

print(a)


# Practice Tasks for Day 1

# Write a program to input your name and age, and print a greeting like:
# "Hello Haresh, you are 21 years old!"

name= input("Enter your name =")
age = int(input("Enter your age ="))
print("Hello",name,"you are", age,"years old!")


# Take two numbers as input and print:
# Sum, Difference, Product, Division

num1= int(input("Enter no 1 ="))
num2= int(input("Enter no 2 ="))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

# Write a program to check if a number is even or odd using %.

number=int(input("enter number  ="))
if number%2==0:
  print("number is even =", number)

else: print("Number is odd", number)
  
# Take a string input "100" and convert it into integer & float, then add +10 to both.
x=input("Enter string =")
y=int(x)
z= float(x)
print(y+10, z+10)