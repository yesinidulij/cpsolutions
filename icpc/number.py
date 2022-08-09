n, m = map(int, input().split())
mi = []
cnt = 0
ans=set()
for _ in range(n):
    li = list(map(str, input().split()))
    mi.extend(li)
for i in range(len(mi)):
    if mi.count(mi[i]) == n:
        string=mi[i]
        cnt += 1
        ans.add(mi[i])

print(cnt // n)
for i in sorted(ans):
    print(i)



