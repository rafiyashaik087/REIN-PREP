n=int(input().strip())
if n<2:
    print(0)
else:
    a=list(map(int,input().strip().split()))
    m1=0
    m2=0
    for i in a:
        if i>m1:
            m2=m1
            m1=i
        elif i>m2:
            m2=i
    if m2==0:
        print(0)
    else:
        print(m1+m2)