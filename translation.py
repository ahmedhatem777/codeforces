# https://codeforces.com/problemset/problem/41/A
original_word = input();
translated_word = input();

if translated_word == original_word[::-1]:
    print('YES');
else:
    print('NO');
