import sys
input = sys.stdin.readline

n = int(input())
dp=[0] * 1000001 

dp[0] = 0
dp[1] = 1
for i in range(2,len(dp)):
    dp[i] = (dp[i-1]%1000000000 + dp[i-2]%1000000000)%1000000000

if n <0 and n%2==0:
    print(-1)
elif n ==0:
    print(0)
else:
    print(1)

print(dp[abs(n)])