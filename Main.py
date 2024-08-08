import math
def add (x,y):
    return x+y
def sub (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    if(y!=0):
        return x/y
    else:
        return "Error! Division by zero."
def sqrt (x):
    if(x>0):
        return math.sqrt(x)
    else:
        return"Error! Cannot take the square root of a negative number."

def calculator ():
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")

    while True:
        choice = input("Enter choice(1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the number 1: "))
            num2 = float(input("Enter the number 2: "))
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1,num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {sub(num1,num2)}")
            elif choice == '3':
                print(f"{num1} X {num2} = {multiply(num1,num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1,num2)}")
        elif choice == '5':
            num = float(input("Enter number: "))
            print(f"√{num} = {sqrt()}")
        else:
            print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if(next_calculation.lower() !="yes"):
            break;

if __name__ == "__main__":
    calculator()
    
