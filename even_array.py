# https://codeforces.com/problemset/problem/1367/B
test_cases = int( input() );

for i in range( test_cases ):
    array_len = int( input() );
    array = [int( i ) for i in input().split()];
    even, odd = 0, 0;

    for i in range( array_len ):
        if array[i] % 2 != i % 2:
            if i % 2 == 0:
                even += 1;
            else:
                odd += 1;
            
    print( even if even == odd else '-1' );