for _ in range(int(input())):
    s, n = map(int, input().split())
    m = s // n
    if (s % n) % 2 != 0:
        if s%n!=1:
         m += 2
        else:
            m+=1
    else:
        if (s%n)!=0:
          m += 1
    print(m)
