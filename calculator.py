def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: Division by zero"

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")

    operation = input("Enter choice (1/2/3/4/5/6/7): ")

    if operation == '1':
        print(f"Result: {add(num1, num2)}")
    elif operation == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif operation == '4':
        print(f"Result: {divide(num1, num2)}")
    elif operation == '5':
        print(f"Result: {modulus(num1, num2)}")
    elif operation == '6':
        print(f"Result: {power(num1, num2)}")
    elif operation == '7':
        print(f"Result: {floor_division(num1, num2)}")
    else:
        print("Invalid operation selected")

if __name__ == "__main__":
    calculator()
