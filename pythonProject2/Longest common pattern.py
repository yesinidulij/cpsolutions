for _ in range(int(input())):
     s=input()
     c=input()
     li=[]
     if len(s)>=len(c):
         for i in range(max(len(s), len(c))):
          if (s[i] in c):
           if s[i] not in li:
               li.extend([s[i]]*min(s.count(s[i]),c.count(s[i])))
     else:
         for i in range(max(len(s), len(c))):
             if (c[i] in s):
                 if c[i] not in li:
                     li.extend([c[i]] * min(s.count(s[i]), c.count(s[i])))
     print(len(''.join(li)))
