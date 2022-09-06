# Function Description:
#     Complete the permutationEquation function in the editor below.
#     permutationEquation has the following parameter(s):
#         int p[n]: an array of integers
#
# Returns:
#     int[n]: the values of `y` for all `x` in the arithmetic sequence 1 to `n`.
#
# Input Format:
#     The first line contains an integer `n`, the number of elements in the sequence.
#     The second line contains `n` space-separated integers p[i] where 1 <= i <= n.

import os


def permutationEquation(p):
    total = []
    for x in range(1, len(p) + 1):
        total.append(p.index(p.index(x) + 1) + 1)
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
