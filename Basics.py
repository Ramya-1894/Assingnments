# 1. Program to print your name
print("D.RAMYA SRI")

# 2. Single line and multi-line comments
print('This is single line comment')
print(''' This is Multi-line comment''')

# 3. Defining variables of different data types and printing them
int_A = 98
bool = True      
char_A = "CODING"       
float_A = 29.6      
double_A  = 45.612356
print("Integer:", int_A)
print("Boolean:", bool)
print("Character:", char_A)
print("Float:", float_A)
print("Double:", double_A)

# 4.Global variable
x = 10  
def my_function():
    x = 20  
    print("Local x:", x)  
print("Global x:", x)  
my_function()
print("Global  variable x after function call:", x)

