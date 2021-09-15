# https://codeforces.com/problemset/problem/158/A
n_k = input().split()
n = int(n_k[0]);
k = int(n_k[1]);
contestants = input();
contestants_list = contestants.split();
i = 0;
qualified = 0;

while i < n:

    qualifying_score = int(contestants_list[k-1]);
    if qualifying_score == 0:
        if( int( contestants_list[i] ) > qualifying_score  ):
            qualified += 1;
        else:
            break;
    else:
        if (int(contestants_list[i]) >= qualifying_score):
            qualified += 1
        else:
            break
    i += 1;

print(qualified);
