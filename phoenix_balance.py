# https://codeforces.com/problemset/problem/1348/A
test_cases = int(input())

for i in range(test_cases):
    array_length = int(input())
    till_mid = 0
    for i in range((array_length // 2) - 1):
        till_mid += 2**(i + 1)
    left_side = 2**(array_length // 2) + till_mid
    right_side = (2**(array_length // 2 + 1) - 2) - left_side

    print(left_side - right_side)
