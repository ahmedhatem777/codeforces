# https://codeforces.com/problemset/problem/431/A
stripes = [int(i) for i in input().split()];
calories = sum([stripes[int(i) - 1] for i in list(input())]);

print(calories)
