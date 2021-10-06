# https://codeforces.com/problemset/problem/490/A
number_of_students = int(input())
student_list = [int(i) for i in input().split()]
programmers = []
mathematicians = []
jocks = []

for i in range(number_of_students):
    if student_list[i] == 1:
        programmers.append(i + 1)
    elif student_list[i] == 2:
        mathematicians.append(i + 1)
    else:
        jocks.append(i + 1)

teams = min(len(programmers), len(mathematicians), len(jocks))
print(teams)

for i in range(teams):
    print(programmers[i], mathematicians[i], jocks[i])