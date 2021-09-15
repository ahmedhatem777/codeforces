number_of_stones = int( input() );
stones = input();
streak = 0;

for i in range( number_of_stones - 1 ):
    if stones[i] == stones[i + 1]:
        streak += 1;

print(streak);
