def calculate_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return (250000 * 0.05) + (income - 500000) * 0.20
    elif income <= 5000000:
        return (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30
    else:
        return (250000 * 0.05) + (500000 * 0.20) + (4000000 * 0.30) + (income - 5000000) * 0.30

def main():
    income = float(input("Enter the annual income: "))
    tax = calculate_tax(income)
    print(f"Income tax amount = {tax:.2f}")

if __name__ == "__main__":
    main()