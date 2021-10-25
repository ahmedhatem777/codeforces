# https://codeforces.com/problemset/problem/1294/A
test_cases = int( input() );

for i in range( test_cases ):
  a_b_c = [int(i) for i in input().split()];
  n = a_b_c.pop(len(a_b_c) - 1);
  maximum = max(a_b_c);
  difference = map( lambda x: maximum - x, a_b_c );
  sum_difference = sum(list(difference));

  if n >= sum_difference:
    if (n - sum_difference) % 3 == 0 or (n - sum_difference) == 0:
      print('YES');
    else:
      print('NO');
  else:
    print('NO');