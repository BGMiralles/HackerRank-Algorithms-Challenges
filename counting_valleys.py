# Function Description:
#     Complete the countingValleys function in the editor below.
#     countingValleys has the following parameter(s):
#         int steps: the number of steps on the hike
#         string path: a string describing the path
#
# Returns:
#     int: the number of valleys traversed
#
# Input Format:
#     The first line contains an integer `steps`, the number of steps in the hike.
#     The second line contains a single string `path`, of `steps` characters that describe the path.

import os


def countingValleys(steps, path):
    valley = 0
    ground = 0
    for x in path:
        if x == 'U':
            ground += 1
        else:
            ground -= 1
        if ground == 0 and x == 'U':
            valley += 1
    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
