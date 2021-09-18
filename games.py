# https://codeforces.com/problemset/problem/268/A
number_of_teams = int( input() );
teams_colors = [];
home_playing_guest = 0;

for i in range(number_of_teams):
    teams_colors.append( input().split() );

for i in range(number_of_teams):
    for j in range(number_of_teams):
        if( teams_colors[i][0] == teams_colors[j][1] or teams_colors[1] == teams_colors[j][0] ):
            home_playing_guest += 1;
        
print( home_playing_guest );
