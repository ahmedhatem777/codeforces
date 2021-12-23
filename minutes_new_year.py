# https://codeforces.com/problemset/problem/1283/A

test_cases = int( input() )

for i in range(test_cases):
    time_now = [int(i) for i in input().split()]
    minutes = (23 - time_now[0])* 60 + (60 - time_now[1])

    print(minutes)