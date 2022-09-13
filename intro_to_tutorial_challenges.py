# Function Description:
#     Complete the introTutorial function in the editor below. It must return an integer representing the zero-based
#     index of `V`.
#     introTutorial has the following parameter(s):
#         int arr[n]: a sorted array of integers
#         int V: an integer to search for
#
# Returns:
#         int: the index of `V` in arr
#         The next section describes the input format. You can often skip it, if you are using included methods or
#         code stubs.
#
# Input Format:
#     The first line contains an integer, `V`, a value to search for.
#     The next line contains an integer, `n`, the size of arr. The last line contains `n` space-separated integers,
#     each a value of arr[i] where 0 <= i < n.
#     The next section describes the constraints and ranges of the input. You should check this section to know the
#     range of the input.

import os


def introTutorial(V, arr):
    for x in arr:
        if V == x:
            return arr.index(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
