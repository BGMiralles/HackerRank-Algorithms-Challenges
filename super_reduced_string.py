# Function Description:
#     Complete the superReducedString function in the editor below.
#     superReducedString has the following parameter(s):
#         string s: a string to reduce
#
# Returns:
#     string: the reduced string or Empty String
#
# Input Format:
#     A single string, `s`.

import os


def superReducedString(s):
    stri = [0]
    for i in s:
        if stri[-1] == i:
            stri.pop()
        else:
            stri.append(i)
    stri.pop(0)
    if stri == []:
        return "Empty String"
    else:
        return "".join(stri)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
