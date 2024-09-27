def fel(n,memo={}):
    if n==0 or n==1:
        return 1
    if n in memo:
        return memo[n]
        res=(fel(n-1,memo)+7*fel(n-2,memo)+n//4)%(10**9+7)
        memo[n]=res
        return res
n=int(input())
print(fel(n))