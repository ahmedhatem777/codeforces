# https://codeforces.com/problemset/problem/151/A
n, k, l, c, d, p, nl, np = map(int, input().split());

lime_slices = c * d;
milliliters = (k * l) // nl;
salt = p // np;

print( min(lime_slices, milliliters, salt) // n);
