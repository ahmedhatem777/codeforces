# https://codeforces.com/problemset/problem/467/A
number_of_rooms = int( input() );
available_rooms = 0;

for i in range(number_of_rooms):
    current_room = input().split();
    inhabiting = int( current_room[0] );
    capacity = int( current_room[1] );

    if( capacity - inhabiting >= 2 ):
        available_rooms += 1;
    
print( available_rooms );