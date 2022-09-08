# Function Description:
#     Complete the beautifulTriplets function in the editor below.
#     beautifulTriplets has the following parameters:
#         int d: the value to match
#         int arr[n]: the sequence, sorted ascending
#
# Returns:
#     int: the number of beautiful triplets
#
# Input Format:
#     The first line contains 2 space-separated integers, `n` and `d`, the length of the sequence and the beautiful
#     difference.
#     The second line contains `n` space-separated integers arr[i].

import os


def beautifulTriplets(d, arr):
    c = 0
    for x in sorted(arr):
        if x + d in arr and x + d + d in arr:
            c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
