# Function Description:
#     Complete the timeConversion function in the editor below. It should return a new string representing the input time
#     in 24 hour format.
#     timeConversion has the following parameter(s):
#         string s: a time in 12 hour format
#
# Returns:
#     string: the time in 24 hour format
#
# Input Format:
#  A single string `s` that represents a time in 12-hour clock format (i.e.:hh:mm:ssAM or hh:mm:ssPM).

import os


def timeConversion(s):
    time = []
    if s[-2:] == 'AM' and s[:2] == '12':
        time.append('00')
        time.append(s[2:-2])
    elif s[-2:] == 'PM' and s[2:] == '12':
        time.append(s[:-2])
    elif s[-2:] == 'PM':
        time.append(str(int(s[:2]) + 12))
        time.append(s[2:-2])
    else:
        time.append(s[:-2])

    return "".join(time)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
