from calculator import Calculator

def main():
    calc = Calculator()
    print("Enter two numbers:")
    a = float(input("First number: "))
    b = float(input("Second number: "))

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        result = calc.add(a, b)
        print(f"Result: {result}")
    elif choice == 2:
        result = calc.subtract(a, b)
        print(f"Result: {result}")
    elif choice == 3:
        result = calc.multiply(a, b)
        print(f"Result: {result}")
    elif choice == 4:
        try:
            result = calc.divide(a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {str(e)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
