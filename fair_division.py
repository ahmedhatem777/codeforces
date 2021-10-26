# https://codeforces.com/problemset/problem/1472/B
test_cases = int( input() )

for i in range(test_cases):
    n_candies = int(input())
    ones, twos = 0, 0
    candies = [int(i) for i in input().split()]

    for j in range( n_candies ):
        if candies[j] == 1: ones += 1
        else: twos += 1

    if ones % 2 == 0 and twos % 2 == 0:
        print('YES')
    elif ones > twos and (ones - (twos * 2)) % 2 == 0:
        print('YES')
    elif twos > ones and ones >= (twos % 2) and ones % 2 == 0:
        print('YES')
    else:
        print('NO')