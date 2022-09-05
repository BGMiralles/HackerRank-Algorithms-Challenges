# Function Description:
#     Complete the hurdleRace function in the editor below.
#     hurdleRace has the following parameter(s):
#         int k: the height the character can jump naturally
#         int height[n]: the heights of each hurdle
#
# Returns:
#     int: the minimum number of doses required, always 0 or more.
#
# Input Format:
#     The first line contains two space-separated integers `n` and `k`, the number of hurdles and the maximum height
#     the character can jump naturally.
#     The second line contains `n` space-separated integers height[i] where 0 <= i < n.

import os


def hurdleRace(k, height):
    maxx = max(height)
    if (maxx - k) < 0:
        return 0
    else:
        return maxx - k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
