n, m, k = map(int, input().split())
li = []
marked = []
cnt = 0
for i in range(n):
    s = input()
    li.append(s)
for i in range(m):
    for j in range(n):
        if li[j][i] not in marked:
            marked.append(li[j][i])
            cnt += 1
        else:
            cnt-=1
print(cnt)
