# https://codeforces.com/problemset/problem/1560/A
test_cases = int( input() );

for i in range( test_cases ):
    k_th_element = int( input() );
    num = 0;

    for i in range(2000):
        if i % 3 != 0 and i % 10 != 3:
            num += 1;
            if num == k_th_element:
                print(i); break;