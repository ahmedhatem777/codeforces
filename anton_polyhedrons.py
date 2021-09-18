# https://codeforces.com/problemset/problem/785/A
number_of_polys = int( input() );
total_faces = 0;

for i in range( number_of_polys ):
    current_poly = input();

    if current_poly == 'Icosahedron': total_faces += 20;
    if current_poly == 'Dodecahedron': total_faces += 12;
    if current_poly == 'Octahedron': total_faces += 8;
    if current_poly == 'Cube': total_faces += 6;
    if current_poly == 'Tetrahedron': total_faces += 4;

print(total_faces);

