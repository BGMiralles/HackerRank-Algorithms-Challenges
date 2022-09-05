# Function Description:
#     Complete the beautifulDays function in the editor below.
#     beautifulDays has the following parameter(s):
#         int i: the starting day number
#         int j: the ending day number
#         int k: the divisor
#
# Returns:
#     int: the number of beautiful days in the range
#
# Input Format:
#     A single line of three space-separated integers describing the respective values of `i`, `j`, and `k`.

import os


def beautifulDays(i, j, k):
    count = 0
    for x in range(i, j + 1):
        minus = str(x)[::-1]
        minus = int(minus)
        if (x - minus) % k == 0:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
