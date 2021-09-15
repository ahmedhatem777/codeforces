# https://codeforces.com/problemset/problem/236/A
user_name = input();
distinct_chars = [];

for i in range( len(user_name) ):
    if user_name[i] not in distinct_chars:
        distinct_chars.append(user_name[i]);

if len(distinct_chars) % 2 == 0:
    print('CHAT WITH HER!');
else:
    print('IGNORE HIM!');
