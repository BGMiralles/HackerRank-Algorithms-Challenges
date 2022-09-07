# Function Description:
#     Complete the squares function in the editor below. It should return an integer representing the number of square
#     integers in the inclusive range from `a` to `b`.
#     squares has the following parameter(s):
#         int a: the lower range boundary
#         int b: the upper range boundary
#
# Returns:
#     int: the number of square integers in the range
#
# Input Format:
#     The first line contains `q`, the number of test cases.
#     Each of the next `q` lines contains two space-separated integers, `a` and `b`, the starting and ending integers
#     in the ranges.

import math
import os


def squares(a, b):
    count = 0
    x = math.ceil(math.sqrt(a))
    while x * x <= b:
        x = x + 1
        count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
