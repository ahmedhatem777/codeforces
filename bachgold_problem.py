# https://codeforces.com/problemset/problem/749/A
integer = int( input() );

if integer % 2 == 0:
    print(integer // 2); print( '2 ' * (integer // 2));
else:
    print( (integer - 1) // 2); print( '2 ' * (integer // 2 - 1) + '3');
