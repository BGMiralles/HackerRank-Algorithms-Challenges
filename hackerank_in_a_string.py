# Function Description:
#     Complete the hackerrankInString function in the editor below.
#     hackerrankInString has the following parameter(s):
#         string s: a string
#
# Returns:
#     string: YES or NO
#
# Input Format:
#     The first line contains an integer `q`, the number of queries.
#     Each of the next `q` lines contains a single query string `s`.

import os


def hackerrankInString(s):
    return 'YES' if re.search(r'h.*a.*c.*k.*e.*r.*r.*a.*n.*k', s) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
