# https://codeforces.com/problemset/problem/155/A
number_of_contests = int( input() );
contests_scores = input().split();
best = int( contests_scores[0] );
worst = int( contests_scores[0] );
amazing = 0;
i = 1;

while i < number_of_contests:
    if int( contests_scores[i] ) > best:
        best = int( contests_scores[i] );
        amazing += 1;
    if int( contests_scores[i] ) < worst:
        worst = int( contests_scores[i] );
        amazing += 1;

    i += 1;

print( amazing );
