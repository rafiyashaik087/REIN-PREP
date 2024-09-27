s=input().strip()
n=int(input())
sm=0
end=len(s)
for i in range(len(s)):
    sm+=ord(s[i])
    if sm>n:
        end=i
        break
res=s[:end] if sm>n else s
print(res)