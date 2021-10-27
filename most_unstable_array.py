# https://codeforces.com/problemset/problem/1353/A
test_cases = int( input() )

for i in range( test_cases ):
    n, m = map( int, input().split() )
    if n == 1: print(0)
    elif n == 2: print(m)
    else: print(m * 2)

