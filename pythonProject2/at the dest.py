for _ in range(int(input())):
    n, k = map(int, input().split())
    ht = list(map(str, input().split()))
    for i in range(k):
        if ht[len(ht) - 1] == 'H':
            ht.pop(len(ht) - 1)
            for i in range(len(ht)):
                if ht[i] == 'H':
                    ht[i] = 'T'
                else:
                    ht[i] = 'H'

        else:
            ht.pop(len(ht) - 1)
    print(ht.count('H'))
