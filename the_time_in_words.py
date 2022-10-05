# Function Description:
#     Complete the timeInWords function in the editor below.
#     timeInWords has the following parameter(s):
#         int h: the hour of the day
#         int m: the minutes after the hour
#
# Returns:
#     string: a time string as described
#
# Input Format:
#     The first line contains `h`, the hours portion The second line contains `m`, the minutes portion

import os


def timeInWords(h, m):
    nums = [
        "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "forteen", "quarter",
        "sixteen", "seventeen", "eighteen", "nineteen",
        "twenty", "twenty one", "twenty two", "twenty three",
        "twenty four", "twenty five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine", "half"
    ]
    num2word = dict(enumerate(nums, 1))

    if m == 0:
        word_time = num2word[h] + " o' clock"
    elif m == 1:
        word_time = num2word[m] + " minute past " + num2word[h]
    elif m == 15:
        word_time = "quarter past " + num2word[h]
    elif 2 <= m <= 29:
        word_time = num2word[m] + " minutes past " + num2word[h]
    elif m == 30:
        word_time = "half past " + num2word[h]
    elif m == 45:
        word_time = "quarter to " + num2word[h + 1]
    elif 31 <= m <= 59:
        word_time = num2word[60 - m] + " minutes to " + num2word[h + 1]

    return word_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
