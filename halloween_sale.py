# Function Description:
#     Complete the howManyGames function in the editor below.
#     howManyGames has the following parameters:
#         int p: the price of the first game
#         int d: the discount from the previous game price
#         int m: the minimum cost of a game
#         int s: the starting budget
#
# Input Format:
#     The first and only line of input contains four space-separated integers `p`, `d`, `m` and `s`.

import os


def howManyGames(p, d, m, s):
    count = 0
    while s >= p:
        s -= p
        p = max(p - d, m)
        count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
