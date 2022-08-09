li=list(map(int,input().split()))
mi=list(map(int,input().split()))
if sum(li)==sum(mi):
    print("Tie")
elif sum(li)>sum(mi):
    print("Gunnar")
else:
    print("Emma")