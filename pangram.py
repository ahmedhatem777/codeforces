# https://codeforces.com/problemset/problem/520/A
string_length = int( input() );
string = set( input().lower() );
set_length = len(string);

if string_length < 26:
    print('NO');
else:
    print('YES' if set_length == 26 else 'NO');