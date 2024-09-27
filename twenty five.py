n=int(input())
s=input()
mx=0
for i in range(n):
    for j in range(i+1,n,2):
        l=j-i+1
        mid=(i+j)//2
        ls=sum(int(s[k])for k in range(i,mid+1))
        rs=sum(int(s[k])for k in range(mid+1,j+1))
        if ls==rs:
            mx=max(mx,l)
print(mx)