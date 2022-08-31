# Function Description:
#     Complete the breakingRecords function in the editor below.
#     breakingRecords has the following parameter(s):
#         int scores[n]: points scored per game
#
# Returns:
#     int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records,
#     and index 1 is for breaking least points records.
#
# Input Format:
#     The first line contains an integer `n`, the number of games.
#     The second line contains `n` space-separated integers describing the respective values of score0, score1,...,
#     score n-1.


import os


def breakingRecords(scores):
    min_re = 0
    max_re = 0
    maxx = scores[0]
    minn = scores[0]
    for x in range(len(scores)):
        if scores[x] > maxx:
            maxx = scores[x]
            max_re += 1
        elif scores[x] < minn:
            minn = scores[x]
            min_re += 1
    final = [max_re, min_re]
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
