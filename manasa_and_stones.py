# Function Description:
#     Complete the stones function in the editor below.
#     stones has the following parameter(s):
#         int n: the number of non-zero stones
#         int a: one possible integer difference
#         int b: another possible integer difference
#
# Returns:
#     int[]: all possible values of the last stone, sorted ascending
#
# Input Format:
#     The first line contains an integer `T`, the number of test cases.
#     Each test case contains 3 lines:
#     - The first line contains `n`, the number of non-zero stones found.
#     - The second line contains `a`, one possible difference
#     - The third line contains `b`, the other possible difference.

import os


def stones(n, a, b):
    s = []
    for i in range(int(n)):
        x = abs(i - (n - 1)) * a
        y = b * (i)
        s.append(x + y)
    s = set(s)
    s = sorted(s)
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
