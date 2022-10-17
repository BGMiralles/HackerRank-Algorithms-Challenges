# Function Description:
#     Complete the icecreamParlor function in the editor below.
#     icecreamParlor has the following parameter(s):
#         int m: the amount of money they have to spend
#         int cost[n]: the cost of each flavor of ice cream
#
# Returns:
#     int[2]: the indices of the prices of the two flavors they buy, sorted ascending
#
# Input Format:
#     The first line contains an integer, `t`, the number of trips to the ice cream parlor. The next `t` sets of lines
#     each describe a visit.
#     Each trip is described as follows:
#         The integer `m`, the amount of money they have pooled.
#         The integer `n`, the number of flavors offered at the time.
#         `n` space-separated integers denoting the cost of each flavor: cost[cost[1],cost[2],...,cost[n]].
#
#         Note: The index within the cost array represents the flavor of the ice cream purchased.

import os


def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == m:
                return [i + 1, j + 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
