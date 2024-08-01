def getArray(size):
    array = []
    print(f"Enter {size} values for the array:")
    for _ in range(size):
        value = int(input())
        array.append(value)
    return array


def displayArray(array):
    print("Array elements are:")
    for value in array:
        print(value, end=" ")


print()


def main():
    size = int(input("Enter the size of the array: "))

    array = getArray(size)
    displayArray(array)


if __name__ == "__main__":
    main()
