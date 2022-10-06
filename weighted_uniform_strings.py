# Function Description:
#     Complete the weightedUniformStrings function in the editor below.
#     weightedUniformStrings has the following parameter(s):
#         - string s: a string
#         - int queries[n]: an array of integers
#
# Returns:
#     - string[n]: an array of strings that answer the queries
#
# Input Format:
#     The first line contains a string `s`, the original string.
#     The second line contains an integer `n`, the number of queries.
#     Each of the next `n` lines contains an integer queries[i], the weight of a uniform subtring of `s` that may or
#     may not exist.

import string
import os


def weightedUniformStrings(s, queries):
    alph = dict(zip(list(string.ascii_lowercase), range(1, 27)))
    chr_values = set()
    temp_chr = ''
    for char in s:
        value = alph[char]
        if char in temp_chr:
            temp_chr += char
            chr_values.add(value * len(temp_chr))
        else:
            temp_chr = char
            chr_values.add(value)
    return ['Yes' if i in chr_values else 'No' for i in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
