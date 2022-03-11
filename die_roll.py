# https://codeforces.com/problemset/problem/9/A
y_w = [int(i) for i in input().split()]
maxi = max(y_w)
if maxi == 6:
  print('1/6')
elif maxi == 5:
  print('1/3')
elif maxi == 4:
  print('1/2')
elif maxi == 3:
  print('2/3')
elif maxi == 2:
  print('5/6')
elif maxi == 1:
  print('1/1')
