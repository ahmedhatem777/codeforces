# https://codeforces.com/problemset/problem/1311/A
test_cases = int( input() )

for i in range( test_cases ):
    a,b = map(int, input().split())
    moves = 0
    
    if a > b:
        if (a - b) % 2 == 0: moves += 1
        else: moves += 2
    elif a < b:
        if (b - a) % 2 != 0: moves += 1
        else: moves += 2
    
    print( moves )