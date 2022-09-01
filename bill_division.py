# Function Description:
#     Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split.
#     Otherwise, it should print the integer amount of money that Brian owes Anna.
#     bonAppetit has the following parameter(s):
#         bill: an array of integers representing the cost of each item ordered
#         k: an integer representing the zero-based index of the item Anna doesn't eat
#         b: the amount of money that Anna contributed to the bill
#
# Input Format:
#     The first line contains two space-separated integers `n` and `k`, the number of items ordered and the 0-based index
#     of the item that Anna did not eat.
#     The second line contains `n` space-separated integers bill[x] where 0 <= x < n.
#     The third line contains an integer, `b` , the amount of money that Brian charged Anna for her share of the bill.
#
# Output Format:
#     If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e.,
#     bcharged - bactual) that Brian must refund to Anna. This will always be an integer.


def bonAppetit(bill, k, b):
    half = (sum(bill) - bill[k]) // 2
    if half == b:
        print('Bon Appetit')
    else:
        print(b - half)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
