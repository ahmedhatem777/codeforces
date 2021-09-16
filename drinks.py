# https://codeforces.com/problemset/problem/200/B
number_of_drinks = int( input() );
drinks = input().split();
_sum = 0;

for i in range(number_of_drinks):
    _sum += int( drinks[i] );

print( _sum / number_of_drinks);