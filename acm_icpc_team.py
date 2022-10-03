# Function Description:
#     Complete the acmTeam function in the editor below.
#     acmTeam has the following parameter(s):
#         string topic: a string of binary digits
#
# Returns:
#     int[2]: the maximum topics and the number of teams that know that many topics
#
# Input Format:
#     The first line contains two space-separated integers `n` and `m`, where `n` is the number of attendees and `m`
#     is the number of topics.
#     Each of the next `n` lines contains a binary string of length `m`.

import os
from itertools import combinations
from collections import Counter


def acmTeam(topic):
    topics = []
    for i in combinations(topic,2):
        r = str(sum(map(int, i)))
        topics.append(len(r)-r.count('0'))
    return max(Counter(topics).items())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
