# Function Description:
#     Complete the organizingContainers function in the editor below.
#     organizingContainers has the following parameter(s):
#         int containter[n][m]: a two dimensional array of integers that represent the number of balls of each color in
#         each container.
#
# Returns:
#     string: either Possible or Impossible
#
# Input Format:
#     The first line contains an integer `q`, the number of queries.
#     Each of the next `q` sets of lines is as follows:
#         The first line contains an integer `n`, the number of containers (rows) and ball types (columns).
#         Each of the next `n` lines contains `n` space-separated integers describing row containers[i].
#
# Output Format:
#     For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix.
#     Otherwise, print Impossible.

import os


def organizingContainers(container):
    rows = [0] * n
    cols = [0] * n
    for i in range(n):
        for j in range(n):
            rows[i] += container[i][j]
            cols[i] += container[j][i]

    if sorted(rows) == sorted(cols):
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
