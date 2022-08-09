for _ in range(int(input())):
    n=int(input())
    ai=list(map(int,input().split()))
    ai.sort()
    i=0
    while i<len(ai):
        if i==0:
            if ai[i] - 0 > 2:
                y = ai[i]
                ai.append(1)
                ai.append(ai[i] - 1)
                ai.remove(y)

        else:
         if ai[i]-ai[i-1]>1:
            if (ai[i-1]+1) and ai[i]-(ai[i-1]+1) not in ai:
                y=ai[i]
                ai.append(ai[i-1]+1 )
                ai.append(ai[i]-(ai[i-1]+1))
                ai.remove(y)
        ai.sort()
        i+=1
    print(ai,len(set(ai)))

