# https://codeforces.com/problemset/problem/791/A
two_bears = input().split();
smaller_bear = int(two_bears[0]);
bigger_bear = int(two_bears[1]);
still_lighter = True;
years = 0;

while still_lighter:
    if smaller_bear <= bigger_bear:
        smaller_bear = smaller_bear * 3;
        bigger_bear = bigger_bear * 2;
        years += 1;
    else:
        still_lighter = False;

print(years);
