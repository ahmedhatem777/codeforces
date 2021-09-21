# https://codeforces.com/problemset/problem/427/A
number_of_events = int( input() );
events = input().split();
police_force = 0;
untreated = 0;

for i in range( number_of_events ):
    if int(events[i]) == -1:
        if police_force > 0:
            police_force -= 1;
        else:
            untreated += 1;
    else:
        police_force += int( events[i] );
    
print( untreated );
