# https://codeforces.com/problemset/problem/1335/A
number_of_tests = int( input() );

for i in range( number_of_tests ):
    current_test = int( input() );

    if current_test % 2 == 0:
        print( (current_test // 2) - 1 );
    else:
        print( current_test // 2 );
