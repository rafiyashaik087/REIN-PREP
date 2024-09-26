n=int(input())
l=list(map(int,input().split()))
dl=[]
for i in range(n-1):
    d=l[i+1]-l[i]
    dl.append(d)
print(" ".join(map(str,dl)))