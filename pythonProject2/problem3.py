record=int(input())
cnt=-1
for i in range(record+1):
     if '2'not in str(i)and'6'not in str(i)and'8'not in str(i)and'0' not in str(i):
        cnt+=1

if record==-1:
    print('')
else:
 print(cnt)