# https://codeforces.com/problemset/problem/1454/A
test_cases = int( input() )

for i in range( test_cases ):
    numba = int( input() )
    right = list(range(1, numba))
    left = [numba]
    answer = left + right
    print( *answer )