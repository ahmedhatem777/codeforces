# https://codeforces.com/problemset/problem/723/A
input_list = input().split();
points = [int( i ) for i in input_list];
points = sorted(points);
print( points[2] - points[0] );