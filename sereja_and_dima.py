# https://codeforces.com/problemset/problem/381/A
array_length = int(input());
arr = list(map(int, input().split()));
s_turn = True;
sereja = 0;
dima = 0;

for i in range(array_length):
    if arr[0] > arr[len(arr) - 1]:
        if s_turn:
            sereja = sereja + arr[0];
        else:
            dima = dima + arr[0];
        del arr[0];
    else:
        if s_turn:
            sereja = sereja + arr[len(arr) - 1];
        else:
            dima = dima + arr[len(arr) - 1];
        del arr[len(arr) - 1];

    s_turn = not s_turn;

print(sereja, dima);