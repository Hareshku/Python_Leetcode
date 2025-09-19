# control flow 
age= int(input("Enter your age = "))
if age>=18:
  print("You are adult")
elif age<18:
  print("You are teenager ")
else:
  print("You are very old")
  
  # loop with range
for i in range(5):
    print(i)

# loop from 1 to 20 
for i in range(1, 21):
  if i%2 == 0:
   print(i, end = "  ")
  elif i%2 == 1:
   print(i, end=" ")
   
print("Even\todd")
for  i in range(1, 20, 2):
     print(f"{i+1}\t{i}")
     
count=1
while count <=5:
  print("count = ",count)
  count+=1

for i in range(10):
  if i==4:
    break
  print(i)
  
for i in range(10):
    pass
  
for i in range(10):
    if i== 5:
      continue
    print(i)


# Practice Tasks for Day 2

# 1 Write a program to print numbers 1 to 20 using:

# for loop
print("Using for loop")
for i in range(1,21):
  print(i)
# while loop
print("Using while loop")
i=1
while i<=20:
  print(i)
  i+=1

# 2 Print the multiplication table of a number given by the user.
number =int(input("Enter the number to generate multiplication table = "))
for i in range(1, 11):
  print(f"{i} X {number} = {number*i}")
  
# 3 Find the sum of numbers from 1 to N (user input).
number=int(input("Enter nth number to find the sum = "))
sum=0
for i in range(1,number+1):
  sum+=i
print("Sum= ",sum)

# 4 Write a program to check if a number is prime.
num = int(input("Enter a number: "))

if num > 1:   # Prime numbers are greater than 1
    for i in range(2, num):
        if num % i == 0:   # divisible by something
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# 👉 Prime number = greater than 1 and divisible only by 1 & itself.

# 5 Print all numbers from 1 to 50, but skip multiples of 5 using continue.
for i in range(1,51):
  if i%5==0:
    continue
  print(i)

