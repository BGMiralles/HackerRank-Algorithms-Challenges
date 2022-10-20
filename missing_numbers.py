# Function Description:
#     Complete the missingNumbers function in the editor below. It should return a sorted array of missing numbers.
#     missingNumbers has the following parameter(s):
#         int arr[n]: the array with missing numbers
#         int brr[m]: the original array of numbers
#
# Returns:
#     int[]: an array of integers
#
# Input Format:
#     There will be four lines of input:
#     n - the size of the first list, arr
#     The next line contains `n` space-separated integers arr[i]
#     m - the size of the second list, brr
#     The next line contains `m` space-separated integers brr[i]

import os
from collections import Counter


def missingNumbers(arr, brr):
    c1 = Counter(arr)
    c2 = Counter(brr)
    if len(arr) >= len(brr):
        c = c1 - c2
    else:
        c = c2 - c1
    print(c)
    return sorted(set(c.elements()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
