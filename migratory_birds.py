# Function Description:
#     Complete the migratoryBirds function in the editor below.
#     migratoryBirds has the following parameter(s):
#         int arr[n]: the types of birds sighted
#
# Returns:
#     int: the lowest type id of the most frequently sighted birds
#
# Input Format:
#     The first line contains an integer, `n`, the size of arr.
#     The second line describes arr as `n` space-separated integers, each a type number of the bird sighted.

import os
from collections import Counter


def migratoryBirds(arr):
    return Counter(sorted(arr)).most_common(1)[0][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
