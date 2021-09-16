# https://codeforces.com/problemset/problem/344/A
number_of_magnets = int(input());
magnet_groups = 0;
counter = 0;
previous_magnet = input()

while counter < number_of_magnets:
    if counter == 0:
        counter += 1;
        magnet_groups += 1;
        continue;
    current_magnet = input()
    if current_magnet != previous_magnet:
        magnet_groups += 1;
        previous_magnet = current_magnet;
    counter += 1;

print(magnet_groups)
