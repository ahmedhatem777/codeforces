n_k = input().split();
number =  int( n_k[0] );
subtract = int( n_k[1] );

for i in range(subtract):
    if number % 10 == 0:
        number = number // 10;
    else:
        number -= 1;

print(number);