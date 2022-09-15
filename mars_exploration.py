# Function Description:
#     Complete the marsExploration function in the editor below.
#     marsExploration has the following parameter(s):
#         string s: the string as received on Earth
#
# Returns:
#     int: the number of letters changed during transmission
#
# Input Format:
#     There is one line of input: a single string, `s`.

import os


def marsExploration(s):
    count = 0
    for i in range(0,len(s) - 2, 3):
            if s[i]!="S" :
                count+=1
            if s[i+1]!="O" :
                count+=1
            if s[i+2]!="S":
                count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
