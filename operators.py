 #5. Function for arithmetic operators
def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
arithmetic_operations(11,8)

# 6. Increment and decrement operators
number = 5
number += 1  
print("Incremented value:", number)
number -= 1  
print("Decremented value:", number)

# 7. Check if two numbers are equal
a=45
b=45
if a==b:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")
# 8. Relational operators
def relational_operators(a, b):
    print("a < b:", a<b)
    print("a <= b:", a<=b)
    print("a > b:", a>b)
    print("a >= b:", a>=b)
relational_operators(8,6)

# 9. Print the smaller and larger number
a=30
b=10
if a>b:
    print("A is bigger than B",a)
else:
    print("B is smaller than A",b)
