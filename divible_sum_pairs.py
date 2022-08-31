# Function Description:
#     Complete the divisibleSumPairs function in the editor below.
#     divisibleSumPairs has the following parameter(s):
#         int n: the length of array `ar`
#         int ar[n]: an array of integers
#         int k: the integer divisor
#
# Returns:
#     - int: the number of pairs
#
# Input Format:
#     The first line contains 2 space-separated integers, `n` and `k`.
#     The second line contains `n` space-separated integers, each a value of arr[x].

import os
from itertools import combinations


def divisibleSumPairs(n, k, ar):
    count = 0
    comb = combinations(ar, 2)
    for x in comb:
        if sum(x) % k == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
