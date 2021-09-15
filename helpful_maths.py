# https://codeforces.com/problemset/problem/339/A
operation = input().split('+');
operation.sort();
result = '';

for i in range( len(operation) ):
    if i == len(operation) -1:
        result = result + operation[i];
    else:
        result = result + operation[i] + '+';

print(result);
