# https://codeforces.com/problemset/problem/266/B
children_time = input().split();
time = int( children_time[1] );
queue = input();
for i in range( time ):
    x = queue.replace('BG', 'GB')
    queue = x;

print( queue );