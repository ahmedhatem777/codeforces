# https://codeforces.com/problemset/problem/707/A
rows, columns = map(int, input().split())
colors = {
    "C": 0,
    "M": 0,
    "Y": 0,
    "W": 0,
    "G": 0,
    "B": 0
}
for i in range( rows ):
    row = input().split();

    for j in row:
        colors[j] += 1;

if colors["C"] > 0 or colors["M"] > 0 or colors["Y"] > 0:
    print('#Color')
else:
    print('#Black&White')