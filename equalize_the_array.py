# Function Description:
#     Complete the equalizeArray function in the editor below.
#     equalizeArray has the following parameter(s):
#         int arr[n]: an array of integers
#
# Returns:
#     int: the minimum number of deletions required
#
# Input Format:
#     The first line contains an integer `n`, the number of elements in arr.
#     The next line contains `n` space-separated integers arr[i].

from collections import Counter
import os


def equalizeArray(arr):
    x = Counter(arr)
    return n - max(x.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
