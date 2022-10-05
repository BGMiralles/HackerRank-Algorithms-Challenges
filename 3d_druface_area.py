# Input Format:
#     The first line contains two space-separated integers `H` and `W` the height and the width of the board respectively.
#     The next `H` lines contains `W` space separated integers. The `Jth` integer in `Ith` line denotes `Aij`.
#
# Output Format:
#     Print the required answer, i.e the price of the toy, in one line.

from itertools import chain
import os


def surfaceArea(A):
    area = H * W * 2
    for row in chain(A, zip(*A)):
        for i in range(1, len(row)):
            area += abs(row[i]-row[i-1])
        area += row[0] + row[-1]
    return area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
