# https://codeforces.com/problemset/problem/581/A
r_b = input().split();
red_socks = int( r_b[0] );
blue_socks = int( r_b[1] );
fashionable_socks = 0;
remainder_socks = 0;

if red_socks > blue_socks:
    fashionable_socks = blue_socks;
    remainder_socks = 0 if (red_socks - blue_socks) == 1 else (red_socks - blue_socks) // 2;
elif red_socks < blue_socks:
    fashionable_socks = red_socks;
    remainder_socks = 0 if (blue_socks - red_socks) == 1 else (blue_socks - red_socks) // 2;
else:
    fashionable_socks = red_socks;
    remainder_socks = 0;

print(fashionable_socks, remainder_socks);