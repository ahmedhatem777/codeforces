# https://codeforces.com/problemset/problem/734/A
number_of_games = int( input() );
games = input();
anton = games.replace('D', '');
danik = games.replace('A', '');

if len(anton) == len(danik):
    print('Friendship');
else:
    print('Anton' if len(anton) > len(danik) else 'Danik')