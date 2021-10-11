# https://codeforces.com/problemset/problem/1399/B
test_cases = int( input() );

for i in range( test_cases ):
    gifts = int( input() );
    candies = [int(i) for i in input().split()];
    oranges = [int(i) for i in input().split()];
    moves = 0
    min_candy = min( candies );
    min_orange = min( oranges );

    for j in range( gifts ):
        moves += max( candies[j] - min_candy, oranges[j] - min_orange);
    
    print( moves );