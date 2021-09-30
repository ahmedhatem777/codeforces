# https://codeforces.com/problemset/problem/732/A
shovel_price, other_coin = map(int, input().split());
i = 1;

while True:
    if ((i * shovel_price) % 10 == 0) or ((i * shovel_price) % 10 == other_coin):
        break;
    i += 1;

print(i);
