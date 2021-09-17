# https://codeforces.com/problemset/problem/1328/A
number_of_tests = int( input() );

for i in range( number_of_tests ):
    test = input().split();
    a = int( test[0] );
    b = int( test[1] );
    
    if( a % b == 0):
        print(0);
    else:
        print( b - (a % b) );

