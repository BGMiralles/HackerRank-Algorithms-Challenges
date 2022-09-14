# Function Description:
#     Complete the camelcase function in the editor below.
#     camelcase has the following parameter(s):
#         string s: the string to analyze
#
# Returns:
#     int: the number of words in `s`
#
# Input Format:
#     A single line containing string `s`.

import os


def camelcase(s):
    count = 1
    for x in s:
        if x == x.upper():
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
