# https://codeforces.com/problemset/problem/1409/A
test_cases = int( input() );

for i in range( test_cases ):
    a, b = map(int, input().split());
    result = 0;

    modulo = abs(a - b) % 10;
    division = abs(a - b) // 10
    result = division + 1 if modulo > 0 else division;

    print(result);
