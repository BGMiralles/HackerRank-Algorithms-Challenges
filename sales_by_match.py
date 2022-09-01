# Function Description:
#     Complete the sockMerchant function in the editor below.
#     sockMerchant has the following parameter(s):
#         int n: the number of socks in the pile
#         int ar[n]: the colors of each sock
#
# Returns:
#     int: the number of pairs
#
# Input Format:
#     The first line contains an integer `n`, the number of socks represented in ar.
#     The second line contains `n` space-separated integers, ar[x], the colors of the socks in the pile.

def sockMerchant(n, ar):
    ar.sort()
    pair = 0
    last = 0
    for x in ar:
        if x == last:
            pair += 1
            last = 0
        else:
            last = x
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
