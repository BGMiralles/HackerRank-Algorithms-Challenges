# Function Description:
#     Complete the getTotalX function in the editor below. It should return the number of integers that are
#     betwen the sets.
#     getTotalX has the following parameter(s):
#         int a[n]: an array of integers
#         int b[m]: an array of integers
#
# Returns:
#         int: the number of integers that are between the sets
#
# Input Format:
#     The first line contains two space-separated integers, `n` and `m`, the number of elements in arrays `a` and `b`.
#     The second line contains `n` distinct space-separated a[i] integers where 0 <= i < n.
#     The third line contains `m` distinct space-separated b[j] integers where 0 <= j < m.

import os


def getTotalX(a, b):
    res = []
    for x in range(a[0], b[0] + 1):
        n = 0
        for i in a:
            if not x % i:
                n += 1
        if n == len(a):
            n = 0
            for k in b:
                if not k % x:
                    n += 1
                if n == len(b):
                    res.append(x)
    return len(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
