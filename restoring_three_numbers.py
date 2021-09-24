# https://codeforces.com/problemset/problem/1154/A
input_str = input().split();
four_sums = [int(i) for i in input_str];
four_sums = sorted(four_sums);
c = four_sums[3] - four_sums[0];
a = four_sums[2] - c;
b = four_sums[0] - a;

print(a, b, c);
 