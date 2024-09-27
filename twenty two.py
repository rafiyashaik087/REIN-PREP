n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(n):
    s1=sum(l[:i])
    s2=sum(l[i+1:])
    if s1==s2:
        print(i+1)
        f=1
        break
if f==0:
    print("NOT FOUND")