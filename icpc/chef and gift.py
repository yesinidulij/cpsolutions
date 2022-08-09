for _ in range(int(input())):
    n, k = map(int, input().split())
    ai = list(map(int, input().split()))
    cnt = 0
    for i in ai:
        if i % 2 == 0:
            cnt += 1
            if cnt >= k:
                print("YES")
                break
    else:
        print("NO")
