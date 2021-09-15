# https://codeforces.com/problemset/problem/116/A
stops = int( input() );
max_cap = 0;
current_cap = 0;

for i in range( stops ):
    exiting_entering = input().split();
    exiting = int(exiting_entering[0]);
    entering = int(exiting_entering[1]);

    current_cap = (current_cap - exiting) + entering;

    if current_cap > max_cap:
        max_cap = current_cap;

print( max_cap );

