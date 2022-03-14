# https://codeforces.com/problemset/problem/1535/A
test_cases = int( input() )

for i in range( test_cases ):
    array = [int(i) for i in input().split()]
    arr1 = array[0:2]
    arr2 = array[2:]

    sorted_arr = sorted(array)
    if (sorted_arr[2] in arr1 and sorted_arr[3] in arr1) or (sorted_arr[2] in arr2 and sorted_arr[3] in arr2):
        print('NO')
    else:
        print('YES')