import math

# Menu function # Calculate option to choose
def menu():
    print("\nCalculator Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Second Power")
    print("6. Square Root")
    print("7. Exit")

# Calculation functions ----------------------------

# Addition the numbers
def addition():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1} + {num2} = {num1 + num2}")

# Subtraction the numbers
def subtraction():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1} - {num2} = {num1 - num2}")

# Multiply the numbers
def multiplication():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1} × {num2} = {num1 * num2}")  
    
# Division the numbers
def division():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print(f"Result: {num1} ÷ {num2} = {num1 / num2}")   

# Second_power the numbers
def second_power():
    num = float(input("Enter a number: "))
    print(f"Result: {num}^2 = {num ** 2}")

# Square_root the numbers
def square_root():
    num = float(input("Enter a number: "))
    if num < 0:
        print("Error: Cannot take square root of negative number")
    else:
        print(f"Result: √{num} = {math.sqrt(num)}")        
# -----------------------------------------------------

# Main program 
# Calculate on your choose
def main():
    while True:  # do loop until press 7
        menu()
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            multiplication()
        elif choice == "4":
            division()
        elif choice == "5":
            second_power()
        elif choice == "6":
            square_root()
        elif choice == "7":
            print("Exiting calculator...")
            break  
        else:
            print("Invalid choice. Please select 1-7.")

main()
