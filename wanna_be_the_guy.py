# https://codeforces.com/problemset/problem/469/A
number_of_levels = int( input() );
x_levels_with_total = input().split();
y_levels_with_total = input().split();
x_levels = x_levels_with_total[1:];
y_levels = y_levels_with_total[1:]
passed_levels = set(x_levels + y_levels);

if '0' in passed_levels:
    passed_levels.remove('0');

if len( passed_levels ) >= number_of_levels:
    print('I become the guy.');
else:
    print('Oh, my keyboard!');