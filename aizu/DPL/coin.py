n,m = (int(x) for x in input().split())
coin = list(map(int, input().split()))
INF = 100000
dp_coins = [INF]*(n+1)
dp_coins[0] = 0

for c in coin:
    for i in range(n+1):
        if i >= c:
            dp_coins[i] = min(dp_coins[i], dp_coins[i-c]+1)

dp_coins[0] = INF
print(dp_coins[n])

