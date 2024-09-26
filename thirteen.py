n=int(input())
a=input().strip()
k=int(input().strip())
if k==0:
    print(0)
else:
    c0=c1=l=res=0
    for i in range(n):
        c0+=a[i]=="0"
        c1+=a[i]=="1"
        while c0>k or c1>k:
            c0-=a[l]=="0"
            c1-=a[l]=="1"
            l+=1
    res+=i-l+1
print(res)