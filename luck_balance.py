# Function Description:
#     Complete the luckBalance function in the editor below.
#     luckBalance has the following parameter(s):
#         int k: the number of important contests Lena can lose
#         int contests[n][2]: a 2D array of integers where each `contests[i] contains two integers that represent the
#         luck balance and importance of the `i` contest
#
# Returns:
#     int: the maximum luck balance achievable
#
# Input Format:
#     The first line contains two space-separated integers `n` and `k`, the number of preliminary contests and the
#     maximum number of important contests Lena can lose.
#     Each of the next `n` lines contains two space-separated integers, `L[i]` and `T[i]`, the contest's luck balance '
#     and its importance rating.

import os


def luckBalance(k, contests):
    imp = []
    unimp = []

    for contest in contests:
        if contest[1] != 0:
            imp.append(contest[0])
        else:
            unimp.append(contest[0])

    imp = sorted(imp, reverse=True)
    return sum(imp[:k]) - sum(imp[k:]) + sum(unimp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
