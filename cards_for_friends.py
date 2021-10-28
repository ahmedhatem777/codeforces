# https://codeforces.com/problemset/problem/1472/A
test_cases = int( input() )

for i in range( test_cases ):
    w, h, n = map( int, input().split() )
    count = 1;

    while True:
        if count >= n: break
        if w % 2 == 0: count *= 2; w = w // 2
        elif h % 2 == 0: count *= 2; h = h // 2
        else: break

    print('YES' if count >= n else 'NO')