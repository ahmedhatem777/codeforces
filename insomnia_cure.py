# https://codeforces.com/problemset/problem/148/A
k_th = int( input() );
l_th = int( input() );
m_th = int( input() );
n_th = int( input() );
number_of_dragons = int( input() );
dealt_with = 0;
i = 1;

while i <= number_of_dragons:
    if (i % k_th == 0) or (i % l_th == 0) or (i % m_th == 0) or (i % n_th == 0) :
        dealt_with += 1;
    i += 1;

print( dealt_with );