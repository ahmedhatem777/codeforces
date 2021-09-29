# https://codeforces.com/problemset/problem/758/A
number_of_citizens = int(input())
citizens_welfare_str = input().split()
citizens_welfare = [int(i) for i in citizens_welfare_str]
citizens_welfare = sorted(citizens_welfare)
wealthiest = citizens_welfare[number_of_citizens - 1]
chancellor_of_the_exchequer_expenditure = 0

for i in range(number_of_citizens):
    chancellor_of_the_exchequer_expenditure += wealthiest - citizens_welfare[i]

print(chancellor_of_the_exchequer_expenditure)
