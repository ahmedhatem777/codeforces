# https://codeforces.com/problemset/problem/1551/A
test_cases = int( input() )

for i in range( test_cases ):
    n = int( input() )
    c_1 = int( (1/3) * n )
    c_2 = int( (1/3) * n ) 

    if n - ( c_1 + c_2 * 2 ) == 1:
        c_1 += 1
    elif n - ( c_1 + c_2 * 2 ) == 2:
        c_2 += 1
    
    print( c_1, c_2 )