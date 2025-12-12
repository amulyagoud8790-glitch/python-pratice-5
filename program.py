# 10  --> 1 2 5 
# 50  --> 1 2 5 10 25
num=int(input("Enter your number to print factors :"))
for i in range(1, (num//2)+1):
    if num%i==0:
        print(i,end=" ")
-------------------------------------------------------------
        
# Write a program to print count of factors of a given number
# 10
  #  1 2 5

# 50  -- 5
count=0
num=int(input("Enter your number to print count of factors :"))
for i in range(1, (num//2)+1):
    if num%i==0:
        count=count+1

print("number of factors: ",count)
---------------------------------------------------------
        



# Write a program to check given number is prime or not
# 2 3 5 7 11 13 17 19 ....
count=0
num=int(input("Enter your number to check it is prime or not :"))
for i in range(1, (num//2)+1):
    if num%i==0:
        count=count+1

if count==1:
    print(num," is a prime number")
else:
    print(num," is not a prime number")
-----------------------------------------------------------------



# Write a program to check given number is perfect number or not
# 6      :  1+2+3  ==6
# 28     : 1+2+4+7+14===28
# 10     : 1+2+5  ===> 8

sum=0
num=int(input("Enter your number to check it is perfect number or not :"))
for i in range(1, (num//2)+1):
    if num%i==0:
        sum=sum+i

if sum==num:
    print(num," is perfect number")
else:
    print(num," is not a perfect number")
-------------------------------------------------------


for i in range(0,5):
    for j in range(0,5):
        print("Hi", end=" ")
---------------------------------
for i in range(0,5):
    for j in range(0,i+1):
        print(i, end=" ")
    print()
----------------------------------------

for row in range(0,6):
    for col in range(0,7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print(" * ",end=" ")
        else:
            print(" ", end="  ")
    print(" ")
------------------------------------------------------

# While loop:
# Write a program to find number of digits in a given number
# Write a program to display the number in reverse order
# Write a program to check given number is palindrom number or not
