distance = int( input() );

if distance <= 5:
    print(1);
elif distance % 5 == 0:
    print( distance // 5 );
else:
    print( distance // 5 + 1);
