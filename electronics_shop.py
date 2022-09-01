# Function Description:
#     Complete the getMoneySpent function in the editor below.
#     getMoneySpent has the following parameter(s):
#         int keyboards[n]: the keyboard prices
#         int drives[m]: the drive prices
#         int b: the budget
#
# Returns:
#         int: the maximum that can be spent, or -1 if it is not possible to buy both items
#
# Input Format:
#     The first line contains three space-separated integers `b`, `n`, and `m`, the budget, the number of keyboard models
#     and the number of USB drive models.
#     The second line contains `n` space-separated integers keyboard[x], the prices of each keyboard model.
#     The third line contains `n` space-separated integers drives, the prices of the USB drives.

import os


def getMoneySpent(keyboards, drives, b):
    max = -1
    for x in keyboards:
        for y in drives:
            if (x + y <= b) and (x + y > max):
                max = x + y
    return max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
