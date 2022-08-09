m,s=map(str,input().split())
sup=s.upper()
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabetup= alphabet.upper()
for i in range(int(m)):
    li = []

    si=input()
    ind=0
    for j in range(len(si)):
     if (si[j] in alphabet and si[j] in s) or si[j]=="_":
         if si[j]=="_":
           li.append(" ")
         else:
             li.append(s[alphabet.index(si[j])])
     elif (si[j] not in alphabet and si[j] not in s) or si[j]=="_":
         if si[j]=="_":
             li.append(" ")
         else:
             li.append(sup[alphabetup.index(si[j])])
    print(''.join(li))


