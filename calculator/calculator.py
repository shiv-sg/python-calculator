from sum import add_numbers
from subtract import subtract_numbers
from multiply import multiply_numbers
from divide import divide_numbers

if __name__=='__main__':
    print("CALCULATOR")
    print("which operation you want to perform")
    print("1. sum")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    operation=input("enter your choice: ")

    if operation=="1":
        print("SUM OF TWO NUMBERS (INTEGER OR DECIMAL)")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("result: ", add_numbers(a, b))
    elif operation=="2":
        print("SUBTRACT OF TWO NUMBERS (INTEGER OR DECIMAL)")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("result: ", subtract_numbers(a, b))
    elif operation=="3":
        print("MULTIPLY OF TWO NUMBERS (INTEGER OR DECIMAL)")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("result: ", multiply_numbers(a, b))
    elif operation=="4":
        print("DIVIDE OF TWO NUMBERS (INTEGER OR DECIMAL)")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("result: ", divide_numbers(a, b))
