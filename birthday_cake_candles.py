# Function Description:
#     Complete the function birthdayCakeCandles in the editor below.
#     birthdayCakeCandles has the following parameter(s):
#         int candles[n]: the candle heights
#
# Returns:
#     int: the number of candles that are tallest
#
# Input Format:
#     The first line contains a single integer, `n`, the size of `candles`.
#     The second line contains `n` space-separated integers, where each integer `i` describes the height of `candles[i]`.


def birthdayCakeCandles(candles):
    return candles.count(max(candles))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
