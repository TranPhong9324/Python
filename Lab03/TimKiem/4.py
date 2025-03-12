#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      PC814
#
# Created:     12/02/2025
# Copyright:   (c) PC814 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def insertionSortRecursive(arr, n):
    if n <= 1:
        return

    insertionSortRecursive(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = last


if __name__ == '__main__':
    A = [-7, 11, 6, 0, -3, 5, 10, 2]
    n = len(A)
    insertionSortRecursive(A, n)
    print(A)


