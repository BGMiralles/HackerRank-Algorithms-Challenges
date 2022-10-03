# Function Description:
#     Complete the encryption function in the editor below.
#     encryption has the following parameter(s):
#         string s: a string to encrypt
#
# Returns:
#     string: the encrypted string
#
# Input Format:
#     One line of text, the string `s` 

import os
import math


def encryption(s):
    s = s.replace(" ","")
    length = len(s)
    c = math.ceil(math.sqrt(length))
    r = math.floor(math.sqrt(length))
    ans = []
    for i in range(c):
        ans.append(s[i::c])
    return ' '.join(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
