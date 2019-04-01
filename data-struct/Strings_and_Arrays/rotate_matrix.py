#!/usr/bin/env python3


def rotate_matrix(matrix):

    N = len(matrix)
    output = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(N-1, -1, -1):
        for k in range(N):
            output[k][j] = matrix[N-1 - j][k]
        #     print("[{}][{}] ---> [{}][{}]".format(N-1 - j, k, k, j))
        # print("---------------------------------------------------")

    return output


def rotate_matrix_pythonic(matrix):

    out = list(zip(*matrix[::-1]))  # still in tuple form
    final = [list(i) for i in out]

    return final


def rotate_matrix_in_place(matrix):

    # Algo source:
    # https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

    N = len(matrix)

    # we only need to do N//2 cycles in an NxN matrix
    # e.g 4x4 matrix, we only need to do the outer layer, and inner layer shift
    for i in range(N//2):
        for j in range(i, N-1-i):

            # put one value in a temp var so that we
            # have "space" to start shifting
            temp = matrix[i][j]

            # shift left value to top value
            matrix[i][j] = matrix[N-1-j][i]

            # shift bottom to left value
            matrix[N-1-j][i] = matrix[N-1-i][N-1-j]

            # shift right to bottom
            matrix[N-1-i][N-1-j] = matrix[j][N-1-i]

            # shift top to right
            matrix[j][N-1-i] = temp

        # for i in matrix:
        #     print(i, end="\n")
        # print("------------------------")

    return matrix


# if __name__ == "__main__":
#     arr = [
#         [1, 2, 3, 4, 5],
#         [6, 7, 8, 9, 10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20],
#         [21, 22, 23, 24, 25]
#     ]

#     rotate_matrix_pythonic(arr)
