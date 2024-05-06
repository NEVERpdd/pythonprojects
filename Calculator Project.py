import os

def main():
    os.system('cls')
    calculator_menu()
    operation()
    finish()

################################################################################

def calculator_menu(): 
    print('Cᴀʟᴄᴜʟᴀᴛᴏʀ\n')   
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
def operation(): 
    choice = input("\nSelect operation (1/2/3/4): ")
    os.system('cls')
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else: 
        if choice > '4':
            print('Choose a valid option (1 - 4)\n')
            finish()

################################################################################

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

################################################################################

def finish():
    input("Press any button to continue...")
    os.system("cls")
    main()

if __name__ == '__main__':
    main()