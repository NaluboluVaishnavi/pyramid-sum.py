#i/p:3
rows = int(input())
ans = 0
for i in range(2,rows+1):
    n = i
    while n>1:
        ans += 2*n
        n = n-1
ans+= rows  
print(ans)      

