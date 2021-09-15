# https://codeforces.com/problemset/problem/263/A
matrix = [[]];
one_location = [];

for i in range(5):
    matrix.insert(i, input().split() );
matrix.pop(5);

for i in range( len(matrix) ):
    if '1' in matrix[i]:
        one_location.insert(0, i + 1);
        one_location.insert(1, matrix[i].index('1') + 1);


print( abs( one_location[0] - 3) + abs( one_location[1] - 3) );
