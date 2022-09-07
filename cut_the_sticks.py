# Function Description:
#     Complete the cutTheSticks function in the editor below. It should return an array of integers representing the
#     number of sticks before each cut operation is performed.
#     cutTheSticks has the following parameter(s):
#         int arr[n]: the lengths of each stick
#
# Returns:
#     int[]: the number of sticks after each iteration
#
# Input Format:
#     The first line contains a single integer `n`, the size of arr.
#     The next line contains `n` space-separated integers, each an arr[i], where each value represents the length
#     of the i stick.

import os


def cutTheSticks(arr):
    lengthlist = []
    while len(arr) >= 1:
        lengthlist.append(len(arr))
        x = min(arr)
        while x in arr:
            arr.remove(x)
    return lengthlist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
