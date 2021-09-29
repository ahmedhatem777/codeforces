# https://codeforces.com/problemset/problem/1399/A

number_of_tests = int(input());
for i in range(number_of_tests):
    array_length = int(input());
    array_str = input().split();
    can_happen = True;
    int_array = [ int(i) for i in array_str ];
    int_array = sorted(int_array);
    i = 1;

    while i < array_length:
        if ( int_array[i] - int_array[i - 1] == 1 or int_array[i] - int_array[i - 1] == 0 ):
            i += 1;
        else:
            can_happen = False;
            break;

    print('YES' if can_happen else 'NO');
