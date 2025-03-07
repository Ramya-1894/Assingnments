# 1. Print "Bright IT Career" ten times using a for loop
for i in range(10):
    print("Bright IT Career")
# 2. Print numbers from 1 to 20 using while loop
num = 1
while num <= 20:
    print(num)
    num += 1

# 3. Program for equal and not equal operators
def equality_notequality(a, b):
    print("a == b:", a == b)
    print("a != b:", a != b)

equality_notequality(15,2)
# 4. Print odd and even numbers
for i in range(1, 40):
    if i % 2 == 0:
        print("Even:",i)
    else:
        print("Odd:",i)
# 5. Print the largest number among three numbers
def largest_number(a, b, c):
    print("Largest number:", max(a, b, c))
largest_number(24,54,31)

# 6. Print even numbers between 10 and 20 using while loop
num = 10
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1
# 7. Print 1 to 10 using do-while loop simulation
num = 1
while True:  
    print(num)
    num += 1
    if num > 10:  
        break
#8.  Program for Armstrong number
num = int(input("Enter a number: "))
n = num
sum_of_cubes = 0
while num > 0:
    digit = num % 10  
    sum_of_cubes += digit ** 3  
    num //= 10 
if sum_of_cubes == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
#9. Write a program to find the prime or not. 
n=int(input())

if n<2:
    print(f"{n} is not a prime number")
else:
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
if prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not  a prime number")

#10. Write a program to palindrome or not. 
n=input()
if n==n[::-1]:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is a palindrome")
#11. Program to check whether a number is EVEN or ODD using switch 
num=int(input("enter:"))

match num%2:
    case 0:
        print(f"{num} is a even ")
    case 1:
        print(f"{num} is a odd ")
#12. Print gender (Male/Female) program according to given M/F using switch
gender = input("Enter gender (M/F): ").strip().upper()

match gender:
    case 'M':
        print("Male")
    case 'F':
        print("Female")
    case _:
        print("Invalid input")
