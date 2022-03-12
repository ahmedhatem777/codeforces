# https://codeforces.com/problemset/problem/1520/B
test_cases = int( input() )

for i in range( test_cases ):
    number = int(input())
    array = list( str(number) )
    left_most_ordinary = array[0] * len(array)
    if len( array ) == 1:
        print( number )
    else:
        if number >= int(left_most_ordinary):
            print( 9 * (len( array ) - 1) + int(array[0]) )
        else:
            print( 9 * (len( array ) - 1) + ( int(array[0]) - 1 ) )