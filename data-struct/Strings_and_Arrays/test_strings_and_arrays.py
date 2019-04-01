#!/usr/bin/env python3

from rotate_matrix import \
    rotate_matrix, \
    rotate_matrix_in_place,\
    rotate_matrix_pythonic


def test_matrix_rotation_even():

    matrix = [[1,   2,     3,     4],
              [5,   6,     7,     8],
              [9,   10,   11,    12],
              [13,  14,   15,    16]]

    output = [[13, 9, 5, 1],
              [14, 10, 6, 2],
              [15, 11, 7, 3],
              [16, 12, 8, 4]]

    assert output == rotate_matrix(matrix)


def test_matrix_rotation_odd():

    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    output = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    assert output == rotate_matrix(arr)


def test_in_place_matrix_rotation_even():

    matrix = [[1,  2,  3,  4,  5,  6],
              [7,  8,  9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35, 36]]

    output = [[31, 25, 19, 13, 7, 1],
              [32, 26, 20, 14, 8, 2],
              [33, 27, 21, 15, 9, 3],
              [34, 28, 22, 16, 10, 4],
              [35, 29, 23, 17, 11, 5],
              [36, 30, 24, 18, 12, 6]]

    assert output == rotate_matrix_in_place(matrix)


def test_in_place_matrix_rotation_odd():

    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

    output = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
    ]

    assert output == rotate_matrix_in_place(arr)


def test_pythonic_matrix_rotation_even():

    matrix = [[1,  2,  3,  4,  5,  6],
              [7,  8,  9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35, 36]]

    output = [[31, 25, 19, 13, 7, 1],
              [32, 26, 20, 14, 8, 2],
              [33, 27, 21, 15, 9, 3],
              [34, 28, 22, 16, 10, 4],
              [35, 29, 23, 17, 11, 5],
              [36, 30, 24, 18, 12, 6]]

    assert output == rotate_matrix_pythonic(matrix)


def test_pythonic_matrix_rotation_odd():

    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

    output = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
    ]

    assert output == rotate_matrix_pythonic(arr)
