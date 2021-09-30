# https://codeforces.com/problemset/problem/472/A
number = int( input() );

if number % 2 == 0:
    print( 8, number - 8);
else:
    print( 9, number - 9);
