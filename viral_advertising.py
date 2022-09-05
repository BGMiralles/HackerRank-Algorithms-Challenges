# Function Description:
#     Complete the viralAdvertising function in the editor below.
#     viralAdvertising has the following parameter(s):
#     int n: the day number to report
#
# Returns:
#     int: the cumulative likes at that day
#
# Input Format:
#     A single integer, `n`, the day number.

import math
import os


def viralAdvertising(n):
    people = 5
    total = 0
    for _ in range(n):
        people_linked = math.floor(people / 2)
        total += people_linked
        people = people_linked * 3
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
