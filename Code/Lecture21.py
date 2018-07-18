# pylint: disable=c
# grades = [100, 98, 70, 20, 88]
# sum(grades)

# def fib(N):
#     """N >= 2"""
#     fib_seq = [0, 1]
#     for _ in range(N - 2):
#         next_number = sum(fib_seq[-2:])
#         fib_seq.append(next_number)
#     return fib_seq
#
#
# fib(10)


def sum_matrix(matrix):
    partial_sum = 0
    for row in matrix:
        for entry in row:
            partial_sum += entry
    return partial_sum


matrix1 = [[2, 1, 3], [4, 5, 7]]
print sum_matrix(matrix1)


def multiply_matrix(matrix, a):
    # Demonstrate the use of indexes vs. direct iteration
    rows = len(matrix)
    cols = len(matrix[0])
    new_mtx = []
    for row_ind in range(rows):
        new_row = []
        for col_ind in range(cols):
            new_row.append(matrix[row_ind][col_ind] * a)
        new_mtx.append(new_row)
    return new_mtx


matrix1 = [[2, 1, 3], [4, 5, 7]]
print multiply_matrix(matrix1, 3)
