# https://codeforces.com/problemset/problem/136/A
friends_number = int( input() );
friends = input().split();
ordered_friends = [0] * len(friends);
answer = '';

for i in range( len(friends) ):
    ordered_friends[ int(friends[i]) - 1] = i + 1;

for i in range( len(ordered_friends) ):
    answer += str( ordered_friends[i] ) + ' ';

print(answer);
