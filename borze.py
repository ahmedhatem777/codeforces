# https://codeforces.com/problemset/problem/32/B

number = list(input())
answer = ''
i = 0

while i < len( number ):
    if number[i] == '.':
        answer = answer + '0'
    elif number[i] + number[i+1] == '-.':
        answer = answer + '1'; i += 1
    elif number[i] + number[i+1] == '--':
        answer = answer + '2'; i += 1
    i += 1

print( answer )