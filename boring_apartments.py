# https://codeforces.com/problemset/problem/1433/A
test_cases = int(input())

for i in range(test_cases):
    apartment = input()
    digit = int(apartment[0])
    length = len(apartment)
    answer = (digit - 1) * 10 + (length * (length + 1)) // 2
    print(answer)
