# https://codeforces.com/problemset/problem/486/A
given_number = int( input() );

if given_number % 2 == 0:
    print( given_number // 2);
else:
    print( (given_number + 1) // 2 * -1 );
