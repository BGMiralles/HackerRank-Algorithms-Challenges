# Function Description:
#     Complete the staircase function in the editor below.
#     staircase has the following parameter(s):
#         int n: an integer
#
# Input Format:
#     A single integer, `n`, denoting the size of the staircase.
#
# Output Format:
#     Print a staircase of size `n` using `#` symbols and spaces.
#     Note: The last line must have 0 spaces in it.

def staircase(n):
    for x in range(1, n + 1):
        print(' ' * (n - x), end='')
        print('#' * x)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
