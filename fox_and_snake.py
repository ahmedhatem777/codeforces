# https://codeforces.com/problemset/problem/510/A
n_m = input().split();
n = int( n_m[0] );
m = int( n_m[1] );
full_hashes = True;
to_right = True;

for i in range(n):
    if full_hashes:
        print('#' * m);
    else:
        if to_right:
            print('.' * (m - 1), end= ''); print('#');
            to_right = not to_right;
        else:
            print('#', end = ''); print('.' * (m - 1));
            to_right = not to_right;
    
    full_hashes = not full_hashes;