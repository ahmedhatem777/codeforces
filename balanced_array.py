# https://codeforces.com/problemset/problem/1343/B
test_cases = int( input() );

for i in range( test_cases ):
    array_length = int( input() );

    if (array_length // 2) % 2 == 0:
        even_list = list( range(2, array_length + 1 , 2) );
        odd_list = list( range(1, array_length + 1, 2) );
        odd_list[len(odd_list) -1 ] += len(odd_list);
        print('YES');
        print( *(even_list + odd_list) );
    else:
        print('NO');