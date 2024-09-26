n=int(input())
a=list(map(int,input().split()))
b=int(input())
a.sort()
s=0
res=0
for i in a:
    if s+i<=b:
        s+=i
        res+=1
print(res)