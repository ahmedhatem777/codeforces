# https://codeforces.com/problemset/problem/1360/B
test_cases = int( input() );

for i in range( test_cases ):
    n = int( input() );
    athletes = sorted([int(i) for i in input().split()]);
    minimum = 1001;

    for i in range(1, n):
        if len(set(athletes)) != len(athletes):
            minimum = 0; break;
        elif athletes[i] - athletes[i - 1] == 1:
            minimum = 1; break;
        elif athletes[i] - athletes[i - 1] < minimum:
            minimum = athletes[i] - athletes[i - 1];
    
    print( minimum );