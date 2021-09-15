# https://codeforces.com/problemset/problem/271/A
given_year = int( input() );
is_unique = False;
year = given_year + 1;
while not is_unique:
    if len( set( str(year) )) == 4:
        is_unique = True;
        break;
    year += 1;

print(year);