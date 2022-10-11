# Function Description:
#     Complete the closestNumbers function in the editor below.
#     closestNumbers has the following parameter(s):
#         int arr[n]: an array of integers
#
# Returns:
#     - int[]: an array of integers as described
#
# Input Format:
#     The first line contains a single integer `n`, the length of arr.
#     The second line contains `n` space-separated integers, arr[i].

import os


def closestNumbers(arr):
    n = len(arr)
    arr.sort()

    diff_dict = {}
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff not in diff_dict:
            diff_dict[diff] = []
        diff_dict[diff].extend([arr[i], arr[i + 1]])

    min_diff = min([k for k in diff_dict])

    return diff_dict[min_diff]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
