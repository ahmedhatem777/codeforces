# https://codeforces.com/problemset/problem/677/A
n_h = input().split();
friends_num = int( n_h[0] );
fence_height = int( n_h[1] );
friends = input().split();
width = 0;

for i in range( friends_num ):
    if int(friends[i]) > fence_height:
        width += 2;
    else:
        width += 1;
    
print( width );

