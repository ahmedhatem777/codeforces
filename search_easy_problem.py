# https://codeforces.com/problemset/problem/1030/A
participants = int( input() );
results = input().split();
is_easy = True;

for i in range( participants ):
    if int(results[i]) == 1:
        is_easy = False;
        break;

print('EASY' if is_easy else 'HARD');
    