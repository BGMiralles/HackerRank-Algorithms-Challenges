# Function Description:
#     Complete the countingSort function in the editor below.
#     countingSort has the following parameter(s):
#         arr[n]: an array of integers
#
# Returns:
#     int[100]: a frequency array
#
# Input Format:
#     The first line contains an integer `n`, the number of items in arr.
#     Each of the next `n` lines contains an integer arr[i] where 0 <= i < n.

import os


def countingSort(arr):
    res = [0] * 100
    for x in range(len(arr)):
        res[arr[x]] += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
