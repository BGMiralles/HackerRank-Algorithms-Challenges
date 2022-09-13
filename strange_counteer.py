# Function Description:
#     Complete the strangeCounter function in the editor below.
#     strangeCounter has the following parameter(s):
#         int t: an integer
#
# Returns:
#     int: the value displayed at time
#
# Input Format:
#     A single integer, the value of `t`.

import os


def strangeCounter(t):
    x = 0
    cycle = 0
    while t > x:
        x = x + 3 * 2 ** cycle
        cycle += 1
    return x - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
