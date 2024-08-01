def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."


def main():
    while True:
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Choose an option (1-5): "))

        if choice == 5:
            break

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("Result: ", addition(num1, num2))
            elif choice == 2:
                print("Result: ", subtraction(num1, num2))
            elif choice == 3:
                print("Result: ", multiplication(num1, num2))
            elif choice == 4:
                print("Result: ", division(num1, num2))
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
