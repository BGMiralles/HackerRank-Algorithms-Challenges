# Function description:
#     Complete the diagonalDifference function in the editor below.
#     diagonalDifference takes the following parameter:
#         int arr[n][m]: an array of integers
#
# Return:
#     int: the absolute diagonal difference
#
# Input Format:
#     The first line contains a single integer, `n`, the number of rows and columns in the square matrix `arr`.
#     Each of the next `n` lines describes a row, `arr[i]`, and consists of `n` space-separated integers `arr[i][j]`.
#
# Output Format:
#     Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

import os


def diagonalDifference(arr):
    prima_diag = sum(arr[i][i] for i in range(n))
    second_diag = sum(arr[i][(n - 1) - i] for i in range(n))
    return abs(prima_diag - second_diag)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
