# https://codeforces.com/problemset/problem/546/A
k_n_w = input().split();
initial_cost = int(k_n_w[0]);
money = int(k_n_w[1]);
bananas = int(k_n_w[2]);
total_cost = 0;
i = 1;

while i < bananas + 1:
    total_cost = total_cost + (initial_cost * i);
    i += 1;

money_to_borrow = total_cost - money;

if money_to_borrow > 0:
    print(money_to_borrow)
else:
    print(0);
