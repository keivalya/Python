# ***
# Program for simple calculator
# ***

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b

print(
    "Please select operation: \n \
    1. Add \n \
    2. Suntract \n \
    3. Multiply \n \
    4. Divide"
)

choice = input("Select what you want to do: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(add(num1,num2))
elif choice == '2':
    print(subtract(num1,num2))
elif choice == '3':
    print(multiply(num1,num2))
elif choice == '4':
    print(division(num1,num2))
else:
    print("Invalid")