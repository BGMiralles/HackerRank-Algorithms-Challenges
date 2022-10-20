# Function Description:
#     Complete the beautifulBinaryString function in the editor below.
#     beautifulBinaryString has the following parameter(s):
#         string b: a string of binary digits
#
# Returns:
#     int: the minimum moves required
#
# Input Format:
#     The first line contains an integer `n`, the length of binary string.
#     The second line contains a single binary string `b`.
#
# Output Format:
#     Print the minimum number of steps needed to make the string beautiful.

import os
import re


def beautifulBinaryString(b):
    pattern = r"010"
    l = re.findall(pattern, b)
    return len(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
