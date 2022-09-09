# Function Description:
#     Complete the fairRations function in the editor below.
#     fairRations has the following parameter(s):
#     int B[N]: the numbers of loaves each persons starts with
#
# Returns:
#     string: the minimum number of loaves required, cast as a string, or 'NO'
#
# Input Format:
#     The first line contains an integer `N`, the number of subjects in the bread line.
#     The second line contains `N` space-separated integers B[i].

import os


def fairRations(B):
    c = 0
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i+1] += 1
            B[i] += 1
            c += 2

    if B[len(B)-1] % 2 != 0:
        return("NO")
    return str(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
