# https://codeforces.com/problemset/problem/228/A
shoes_list = input().split();
shoes_set = set(shoes_list)
print(len(shoes_list) - len(shoes_set))
