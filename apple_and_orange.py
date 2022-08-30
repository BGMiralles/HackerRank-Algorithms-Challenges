# Function Description:
#     Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges
#     that land on Sam's house, each on a separate line.
#     countApplesAndOranges has the following parameter(s):
#         s: integer, starting point of Sam's house location.
#         t: integer, ending location of Sam's house location.
#         a: integer, location of the Apple tree.
#         b: integer, location of the Orange tree.
#         apples: integer array, distances at which each apple falls from the tree.
#         oranges: integer array, distances at which each orange falls from the tree.
#
# Input Format:
#     The first line contains two space-separated integers denoting the respective values of `s` and `t`.
#     The second line contains two space-separated integers denoting the respective values of `a` and `b`.
#     The third line contains two space-separated integers denoting the respective values of `m` and `n`.
#     The fourth line contains `m` space-separated integers denoting the respective distances that each apple falls
#     from point `a`.
#     The fifth line contains `n` space-separated integers denoting the respective distances that each orange falls
#     from point `b`.
#
# Output Format:
#     Print two integers on two different lines:
#         The first integer: the number of apples that fall on Sam's house.
#         The second integer: the number of oranges that fall on Sam's house.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples = 0
    total_oranges = 0
    for x in range(len(apples)):
        if a + apples[x] in range(s, t + 1):
            total_apples += 1
    for x in range(len(oranges)):
        if b + oranges[x] in range(s, t + 1):
            total_oranges += 1
    print(total_apples, total_oranges, sep="\n")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)