# https://codeforces.com/problemset/problem/1367/A
test_cases = int( input() );

for i in range(test_cases):
    string = input();
    result = string[0:len(string):2] + string[len(string)-1];
    print(result);