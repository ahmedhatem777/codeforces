# https://codeforces.com/problemset/problem/71/A
iterations = int(input());
i = 0;

while i < iterations:
    word = input();
    if len(word) <= 10:
        print(word);
    else:
        print(word[0:1] + str(len(word) - 2) + word[len(word) -1: len(word)]);
    i += 1;
