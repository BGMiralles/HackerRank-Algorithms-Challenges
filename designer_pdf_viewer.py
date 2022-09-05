# Function Description:
#     Complete the designerPdfViewer function in the editor below.
#     designerPdfViewer has the following parameter(s):
#         int h[26]: the heights of each letter
#         string word: a string
#
# Returns:
#     int: the size of the highlighted area
#
# Input Format:
#     The first line contains 26 space-separated integers describing the respective heights of each consecutive lowercase
#     English letter, ascii[a-z].
#     The second line contains a single word consisting of lowercase English alphabetic letters.

import os
import string


def designerPdfViewer(h, word):
    maxx = []
    a = string.ascii_lowercase
    for letter in word:
        maxx.append(h[a.index(letter)])
    return max(maxx) * len(word)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
