n=int(input())
l=list(map(int,input().split()))
l.sort()
lt,rt=0,0
s=0
for i in range(n//2):
    lt,rt=l[i],l[n-i-1]
    s+=abs(lt-rt)
print(s)