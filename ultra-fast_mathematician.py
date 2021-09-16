# https://codeforces.com/problemset/problem/61/A
first_number = input();
second_number = input();
result = '';

for i in range( len(first_number) ):
    if first_number[i] == second_number[i]:
        result += '0';
    else:
        result += '1';

print( result );