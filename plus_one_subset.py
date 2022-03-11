# https://codeforces.com/problemset/problem/1624/A
test_cases = int( input() )

for i in range( test_cases ):
    array_len = int( input() )
    array = [int(i) for i in input().split()]
    print( max(array) - min(array) )