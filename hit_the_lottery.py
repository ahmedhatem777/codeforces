# https://codeforces.com/problemset/problem/996/A
total_balance = int( input() );
bills = 0;

while total_balance > 0:    
    
    if total_balance >= 100:
        bills += total_balance // 100;
        total_balance = total_balance % 100;
    elif total_balance >= 20:
        bills += total_balance // 20;
        total_balance = total_balance % 20;
    elif total_balance >= 10:
        bills += 1;
        total_balance = total_balance % 10;
    elif total_balance >= 5:
        bills += 1;
        total_balance = total_balance % 5;
    else:
        bills += total_balance;
        total_balance = 0;

print( bills );