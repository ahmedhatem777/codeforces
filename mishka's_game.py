# https://codeforces.com/problemset/problem/703/A
rounds = int( input() );
m, c = 0, 0;

for i in range( rounds ):
    m_round, c_round = map( int, input().split() );

    if m_round > c_round:
        m += 1;
    elif m_round < c_round:
        c += 1;

if m > c:
    print( 'Mishka' );
elif m < c:
    print( 'Chris' );
else:
    print( 'Friendship is magic!^^' );
