# Function Description:
#     Complete the flatlandSpaceStations function in the editor below.
#     flatlandSpaceStations has the following parameter(s):
#         int n: the number of cities
#         int c[m]: the indices of cities with a space station
#
# Returns:
#     - int: the maximum distance any city is from a space station
#
# Input Format:
#     The first line consists of two space-separated integers, `n` and `m`.
#     The second line contains `m` space-separated integers, the indices of each city that has a space-station.
#     These values are unordered and distinct.

import os


def flatlandSpaceStations(n, c):
    max_distance = 0
    c.sort()
    max_distance = max(c[0], n-1-c[-1])
    for i in range(len(c)-1):
        max_distance = max((c[i+1]-c[i])//2,max_distance)

    return max_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
