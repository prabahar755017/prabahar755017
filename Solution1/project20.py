def get_matrix(size, matrix_number):
    """Function to get matrix input from the user."""
    print(f"Enter the values of array {matrix_number}:")
    matrix = []
    for i in range(size):
        row = list(map(int, input().split()))
        if len(row) != size:
            print(f"Error: Expected {size} values, got {len(row)}")
            return None
        matrix.append(row)
    return matrix


def add_matrices(matrix1, matrix2):
    """Function to add two matrices."""
    size = len(matrix1)
    result = []
    for i in range(size):
        result_row = [matrix1[i][j] + matrix2[i][j] for j in range(size)]
        result.append(result_row)
    return result


def print_matrix(matrix):
    """Function to print a matrix."""
    for row in matrix:
        print(' '.join(map(str, row)))


def main():
    size = int(input("Enter the size of arrays: "))

    matrix1 = get_matrix(size, 1)
    if matrix1 is None:
        return

    matrix2 = get_matrix(size, 2)
    if matrix2 is None:
        return

    sum_matrix = add_matrices(matrix1, matrix2)

    print("Sum of 2 arrays is:")
    print_matrix(sum_matrix)


if __name__ == "__main__":
    main()