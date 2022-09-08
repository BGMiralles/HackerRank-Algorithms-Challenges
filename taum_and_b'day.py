# Function Description:
#     Complete the function taumBday in the editor below. It should return the minimal cost of obtaining the desired
#     gifts.
#     taumBday has the following parameter(s):
#         int b: the number of black gifts
#         int w: the number of white gifts
#         int bc: the cost of a black gift
#         int wc: the cost of a white gift
#         int z: the cost to convert one color gift to the other color
#
# Returns:
#     int: the minimum cost to purchase the gifts
#
# Input Format:
#     The first line will contain an integer `t`, the number of test cases.
#     The next `t` pairs of lines are as follows:
#         - The first line contains the values of integers `b` and `w`.
#         - The next line contains the values of integers `bc`, `wc`, and `z`.
#
# Output Format:
#     `t` lines, each containing an integer: the minimum amount of units Taum needs to spend on gifts.

import os


def taumBday(b, w, bc, wc, z):
    if bc > wc + z:
        bc = wc + z
    elif wc > bc + z:
        wc = bc + z
    return b * bc + w * wc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
