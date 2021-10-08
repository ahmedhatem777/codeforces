# https://codeforces.com/problemset/problem/1374/A
test_cases = int( input() );

for i in range( test_cases ):
    x, y, n = map( int, input().split() );

    if n % x != y:
        if n % x < y:
            print( n - (x - (y - n % x)) );
        else:
            print(n - ((n % x) - y))
    else:
        print( n );
