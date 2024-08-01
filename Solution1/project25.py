def main():
    pattern = []
    for i in range(1, 11):
        if i % 2 != 0:
            pattern.extend(['*'] * (i + 2))
        else:
            pattern.extend(['*'])

    index = 0
    for i in range(1, 7):
        print(" ".join(pattern[index:index + i]))
        index += i


if __name__ == "__main__":
    main()