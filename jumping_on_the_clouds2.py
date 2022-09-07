# Function Description:
#     Complete the jumpingOnClouds function in the editor below.
#     jumpingOnClouds has the following parameter(s):
#         int c[n]: an array of binary integers
#
# Returns:
#     int: the minimum number of jumps required
#
# Input Format:
#     The first line contains an integer `n`, the total number of clouds. The second line contains `n` space-separated
#     binary integers describing clouds c[i] where 0 <= i < n.
#
# Output Format:
#     Print the minimum number of jumps needed to win the game.

import os


def jumpingOnClouds(c):
    count = 0
    jump = 0
    while jump < (len(c) - 1):
        if jump + 2 > (len(c) - 1):
            count += 1
            break
        if c[jump + 2] == 0:
            count += 1
            jump += 2
        else:
            count += 1
            jump += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
