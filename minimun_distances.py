# Function Description:
#     Complete the minimumDistances function in the editor below.
#     minimumDistances has the following parameter(s):
#         int a[n]: an array of integers
#
# Returns:
#     int: the minimum distance found or -1 if there are no matching elements
#
# Input Format:
#     The first line contains an integer `n`, the size of array `a`.
#     The second line contains `n` space-separated integers a[i].

import os


def minimumDistances(a):
    ans = []
    for x in range(len(a)):
        for y in range(x):
            if a[x] == a[y]:
                ans.append(abs(x - y))
    if len(ans) > 0:
        return min(ans)
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
