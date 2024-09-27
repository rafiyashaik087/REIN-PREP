n=int(input())
l=list(map(int,input().split()))
res=[]
for i in l:
    res.append(i*6)
print(sum(res))