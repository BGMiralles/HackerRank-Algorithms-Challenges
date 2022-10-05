# Function Description:
#     Complete the happyLadybugs function in the editor below.
#     happyLadybugs has the following parameters:
#         string b: the initial positions and colors of the ladybugs
#
# Returns:
#     string: either YES or NO
#
# Input Format:
#     The first line contains an integer `g`, the number of games.
#     The next `g` pairs of lines are in the following format:
#         The first line contains an integer `n`, the number of cells on the board.
#         The second line contains a string `b` that describes the `n` cells of the board.

from collections import Counter
import os


def happyLadybugs(b):
    n = len(b)
    counter = Counter(b)
    for x in counter:
        if counter[x] == 1 and x != '_':
            return 'NO'
    if '_' in counter:
        return 'YES'
    else:
        count = 0
        ind = b[0]
        for y in range(1, n):
            if b[y] != ind:
                ind = b[y]
                count += 1
            else:
                count = 0
            if count > 1:
                return 'NO'
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
