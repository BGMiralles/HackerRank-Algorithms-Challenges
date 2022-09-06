# Function Description:
#     Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.
#     appendAndDelete has the following parameter(s):
#         string s: the initial string
#         string t: the desired string
#         int k: the exact number of operations that must be performed
#
# Returns:
#     string: either Yes or No
#
# Input Format:
#     The first line contains a string `s`, the initial string.
#     The second line contains a string `t`, the desired final string.
#     The third line contains an integer `k`, the number of operations.

import os


def appendAndDelete(s, t, k):
    len_s, len_t = len(s), len(t)
    match = 0
    for x in range(min(len_s, len_t)):
        if t[x] != s[x]:
            break
        match += 1
    if (len_t + len_s) - 2 * match > k or len_s - match % k == k % 2:
        return "No"
    return "Yes"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
