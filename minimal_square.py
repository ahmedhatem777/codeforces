# https://codeforces.com/problemset/problem/1360/A
test_cases = int( input() );

for i in range( test_cases ):
    arr = sorted(map(int, input().split()));
    side = max( arr[0] * 2, arr[1] );
    print( side**2 );