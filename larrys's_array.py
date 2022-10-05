# Function Description:
#     Complete the larrysArray function in the editor below. It must return a string, either YES or NO.
#     larrysArray has the following parameter(s):
#         A: an array of integers
#
# Input Format:
#     The first line contains an integer `t`, the number of test cases.
#     The next `t` pairs of lines are as follows:
#         The first line contains an integer `n`, the length of `A`.
#         The next line contains `n` space-separated integers A[i].

import os


def larrysArray(A):
    n = len(A)
    s = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                s += 1
    if s % 2 == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
