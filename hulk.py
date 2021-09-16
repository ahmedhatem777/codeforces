# https://codeforces.com/problemset/problem/705/A
given_number = int( input() );
hulk_says = '';
love = False;

for i in range(given_number):
    if not love:
        hulk_says = hulk_says + 'I hate';
    else:
        hulk_says = hulk_says + 'I love';
    
    if i == given_number - 1:
        hulk_says = hulk_says + ' it';
    else:
        hulk_says = hulk_says + ' that ';
    love = not love

print(hulk_says);