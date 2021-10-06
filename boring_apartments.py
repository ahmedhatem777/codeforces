# https://codeforces.com/problemset/problem/1520/A
test_cases = int(input())

for i in range(test_cases):
    days = int(input())
    tasks = list(input())
    unique_tasks = set()
    flag = True

    for i in range(days):
        if tasks[i] in unique_tasks and tasks[i] != tasks[i - 1]:
            flag = not flag
            break
        else:
            unique_tasks.add(tasks[i])

    print('YES' if flag else 'NO')
