# https://codeforces.com/problemset/problem/1512/A
test_cases = int(input())

for i in range(test_cases):
    array_length = int(input())
    array = input().split()
    a_set = set(array)
    dictionary = dict.fromkeys(a_set, 0)

    for i in range(array_length):
        dictionary[array[i]] += 1

        if dictionary[array[i]] > 1:
            a_set.remove(array[i])
            break

    print(array.index(a_set.pop()) + 1)
