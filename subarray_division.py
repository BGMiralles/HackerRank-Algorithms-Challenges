# Function Description:
#     Complete the birthday function in the editor below.
#     birthday has the following parameter(s):
#         int s[n]: the numbers on each of the squares of chocolate
#         int d: Ron's birth day
#         int m: Ron's birth month
#
# Returns:
#         int: the number of ways the bar can be divided
#
# Input Format:
#     The first line contains an integer `n`, the number of squares in the chocolate bar.
#     The second line contains `n` space-separated integers s[x], the numbers on the chocolate squares where 0 <= x < n.
#     The third line contains two space-separated integers, `d` and `m`, Ron's birth day and his birth month.

import os


def birthday(s, d, m):
    count = 0
    for x in range(n + 1):
        if d == sum(s[x:x + m]):
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()