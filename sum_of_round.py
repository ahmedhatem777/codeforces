# https://codeforces.com/problemset/problem/1352/A
test_cases = int( input() );

for i in range( test_cases ):
    number = input();
    i = len(list(number));
    number = int(number);
    divisor = 10;
    answer = [];

    while i > 0:
        if i == 1:
            answer.append(number);
            break;
        if number % divisor != 0:
            answer.append( number % divisor );
            number = number - (number % divisor);
        i -= 1;
        divisor = divisor * 10;

    print( len(answer) );
    for i in answer: print(i, end=' ');