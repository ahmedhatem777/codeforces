# https://codeforces.com/problemset/problem/750/A
n_k = input().split();
n_of_questions = int( n_k[0] );
total_minutes = int( n_k[1] );
questions_answered = 0;
i = 1;

while i <= n_of_questions:
    if total_minutes + (5 * i) <= 240:
        total_minutes += (5 * i);
        questions_answered += 1;
    else:
        break;
    i += 1;

print( questions_answered );