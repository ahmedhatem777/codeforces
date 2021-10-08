# https://codeforces.com/problemset/problem/1353/B
test_cases = int( input() );

for i in range( test_cases ):
    n, k = map( int, input().split() );
    a = sorted([int(i) for i in input().split()]);
    b = sorted([int(i) for i in input().split()], reverse = True);

    for i in range( k ):
        if a[i] < b[i]:
            a[i] = b[i];
        else: 
            break;
    
    print( sum(a) );