# https://codeforces.com/problemset/problem/144/A
number_of_soldiers = int( input() );
soldiers_str = input().split();
soldiers_int = [int(numeric_string) for numeric_string in soldiers_str]

tallest_index = soldiers_int.index(max(soldiers_int));
soldiers_int.reverse();
shortest_index = soldiers_int.index(min(soldiers_int));

if( tallest_index >= (number_of_soldiers - shortest_index) ):
    print((tallest_index + shortest_index) - 1);
else:
    print(tallest_index + shortest_index);
