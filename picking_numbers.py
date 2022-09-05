# Function Description:
#     Complete the pickingNumbers function in the editor below.
#     pickingNumbers has the following parameter(s):
#         int a[n]: an array of integers
#
# Returns:
#     int: the length of the longest subarray that meets the criterion
#
# Input Format:
#     The first line contains a single integer `n`, the size of the array `a`.
#     The second line contains `n` space-separated integers, each an a[x].

import os


def pickingNumbers(a):
    answer = []
    for x in range(0, n):
        answer.append(abs(a.count(a[x])+a.count(a[x]-1)))
    return max(answer)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
