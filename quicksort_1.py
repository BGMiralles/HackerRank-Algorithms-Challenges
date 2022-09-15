# Function Description:
#     Complete the quickSort function in the editor below.
#     quickSort has the following parameter(s):
#         int arr[n]: arr[0] is the pivot element
#
# Returns:
#     int[n]: an array of integers as described above
#
# Input Format:
#  The first line contains `n`, the size of arr.
#     The second line contains `n` space-separated integers arr[i] (the unsorted array). The first integer, arr[0],
#     is the pivot element, `p`.

import os


def quickSort(arr):
    left, right, equal = [], [], []
    for x in arr:
        if x == arr[0]:
            equal.append(x)
        elif x < arr[0]:
            left.append(x)
        else:
            right.append(x)
    return left + equal + right


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
