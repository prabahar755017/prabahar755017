num = int(input("Enter the number:"))
result = 0

for x in range(num):
    if x % 2 == 1:
        result = result + x

print("Sum of odd number is ", result)

