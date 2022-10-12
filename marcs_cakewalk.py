# Function Description:
#     Complete the marcsCakewalk function in the editor below.
#     marcsCakewalk has the following parameter(s):
#         int calorie[n]: the calorie counts for each cupcake
#
# Returns:
#     long: the minimum miles necessary
#
# Input Format:
#     The first line contains an integer `n`, the number of cupcakes in `calorie`.
#     The second line contains `n` space-separated integers, `calorie[i]`.

import os


def marcsCakewalk(calorie):
    min_cal, calorie = 0, sorted(calorie, reverse=True)
    for i in range(len(calorie)):
        min_cal += (calorie[i] * (2 ** i))
    return min_cal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
