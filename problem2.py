str1 = int(input("enter the number:"))


def string_1(str):
    if str % 2 == 0:
        return "the number is even"
    else:
        return "the number is odd"

print(string_1(str1))