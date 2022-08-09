for _ in range(int(input())):
    n,x=map(int,input().split())
    if n>=2*x-1:
     ans=['a' for i in range(n)]
     for i in range(x):
         ans[i]=chr(ord('a')+i)
         ans[-(i+1)]=chr(ord('a')+i)
     print(''.join(ans))
    else:
        print(-1)
