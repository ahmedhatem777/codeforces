# https://codeforces.com/problemset/problem/112/A
first_string = input();
second_string = input();

if first_string.lower() < second_string.lower():
    print(-1);
elif first_string.lower() > second_string.lower():
    print(1);
else:
    print(0);