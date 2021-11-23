# https://codeforces.com/problemset/problem/1385/B
test_cases = int( input() )

for i in range( test_cases ):
    a_length = int(input()) * 2
    a = [int(i) for i in input().split()]
    p = []
    
    for j in range( a_length ):
        if a[j] not in p:
            p.append( a[j] )
    
    print( *p )