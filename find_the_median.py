# Function Description:
#     Complete the findMedian function in the editor below.
#     findMedian has the following parameter(s):
#         int arr[n]: an unsorted array of integers
#
# Returns:
#     int: the median of the array
#
# Input Format:
#     The first line contains the integer `n`, the size of arr.
#     The second line contains `n` space-separated integers arr[i].

import math
import os


def findMedian(arr):
    if n == 1:
        return arr[0]
    ar = sorted(arr)
    if len(arr) % 2 != 0:
        a = (len(arr) // 2)
        return ar[a]
    else:
        b = math.ceil(len(arr) / 2)
        c = b + 1
        return (ar[b] + ar[c]) / 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
