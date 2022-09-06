# Function Description:
#     Complete the jumpingOnClouds function in the editor below.
#     jumpingOnClouds has the following parameter(s):
#         int c[n]: the cloud types along the path
#         int k: the length of one jump
#
# Returns:
#     int: the energy level remaining.
#
# Input Format:
#     The first line contains two space-separated integers, `n` and `k`, the number of clouds and the jump distance.
#     The second line contains `n` space-separated integers c[i] where 0<= i < n. Each cloud is described as follows:
#     If c[i] = 0, then cloud `i` is a cumulus cloud.
#     If c[i] = 1, then cloud `i` is a thunderhead.

import os


def jumpingOnClouds(c, k):
    jump = 0
    energy = 100
    while True:
        energy = energy - 1 - 2 * c[jump]
        jump = (jump + k) % len(c)
        if jump == 0:
            return energy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
