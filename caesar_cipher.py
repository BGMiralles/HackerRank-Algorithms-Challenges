# Function Description:
#     Complete the caesarCipher function in the editor below.
#     caesarCipher has the following parameter(s):
#         string s: cleartext
#         int k: the alphabet rotation factor
#
# Returns:
#     string: the encrypted string
#
# Input Format:
#     The first line contains the integer, `n`, the length of the unencrypted string.
#     The second line contains the unencrypted string, `s`.
#     The third line contains `k`, the number of letters to rotate the alphabet by.

import os


def caesarCipher(s, k):
    k = k % 26
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alpha = alpha[k - 26:] + alpha[:k - 26]
    upper_alpha = ''.join(map(str.upper, alpha))

    result = ''
    for x in s:
        if x in alpha:
            result += rotated_alpha[alpha.find(x)]
        elif x in upper_alpha:
            result += rotated_alpha[upper_alpha.find(x)].upper()
        else:
            result += x
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
