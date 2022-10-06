# Function Description:
#     Complete the countingSort function in the editor below. It should return the original array, sorted ascending,
#     as an array of integers.
#     countingSort has the following parameter(s):
#         arr: an array of integers
#
# Input Format:
#     The first line contains an integer `n`, the length of arr. The next line contains space-separated integers arr[i]
#     where 0 <= i < n.
#
# Output Format:
#     Print the sorted list as a single line of space-separated integers.

import os


def countingSort(arr):
    arr.sort()
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
