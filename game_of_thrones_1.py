# Function Description:
#     Complete the gameOfThrones function below.
#     gameOfThrones has the following parameter(s):
#         string s: a string to analyze
#
# Returns:
#     string: either YES or NO
#
# Input Format:
#     A single line which contains `s`.

import os


def gameOfThrones(s):
    ocount = 0
    check = ''
    for i in s:
        if i not in check:
            check += i
            if s.count(i) % 2 != 0:
                ocount += 1
            if ocount > 1:
                return ('NO')
    return ('YES')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
