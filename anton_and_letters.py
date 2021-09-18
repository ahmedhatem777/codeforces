# https://codeforces.com/problemset/problem/443/A
numbers_string = input();
without_braces = numbers_string.replace('{', '').replace('}', '');
without_commas = without_braces.replace(',', '');

numbers_set = set( without_commas.split() );

print(len(numbers_set) );

