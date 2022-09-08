# Function Description:
#     Complete the chocolateFeast function in the editor below.
#     chocolateFeast has the following parameter(s):
#         int n: Bobby's initial amount of money
#         int c: the cost of a chocolate bar
#         int m: the number of wrappers he can turn in for a free bar
#
# Returns:
#     int: the number of chocolates Bobby can eat after taking full advantage of the promotion
#     Note: Little Bobby will always turn in his wrappers if he has enough to get a free chocolate.
#
# Input Format:
#     The first line contains an integer, `t`, the number of test cases to analyze.
#     Each of the next `t` lines contains three space-separated integers: `n`, `c`, and `m`. They represent money to
#     spend, cost of a chocolate, and the number of wrappers he can turn in for a free chocolate.

import os


def chocolateFeast(n, c, m):
    chocolate = n // c
    wrap = chocolate
    while wrap >= m:
        chocolate += wrap // m
        wrap = wrap // m + wrap % m
    return chocolate


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
