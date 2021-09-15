# https://codeforces.com/problemset/problem/110/A
given_number = int( input() );
lucky_nums = 0;

for i in range( len( str(given_number) )):
    last_number = given_number % 10;
    if last_number == 4 or last_number == 7:
        lucky_nums += 1;
    given_number = given_number // 10;

print('YES' if lucky_nums == 4 or lucky_nums == 7 else 'NO')
