# https://codeforces.com/problemset/problem/141/A
first_word = list(input());
second_word = list(input());
shuffled = list(input());

words_combined = first_word + second_word;
words_combined.sort();
shuffled.sort();

print('YES' if words_combined == shuffled else 'NO');
