# https://codeforces.com/problemset/problem/231/A
iterations = int( input() );
i = 0;
to_solve = 0;

while i < iterations:
    string = input();
    # first and second or first and third or second and third
    if bool( int(string[0:1] )) and bool(int(string[2:3])) or bool( int(string[0:1] )) and bool(int(string[4:5])) or bool(int(string[2:3])) and bool(int(string[4:5])):
        to_solve += 1;
    i += 1;

print(to_solve);
