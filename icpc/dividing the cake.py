for _ in range(int(input())):
    n=int(input())
    li=[1,2,3,4,5,6,8,9,10,12,15,18,20,24,36,40,45,60,72,90,120,180,360]
    ans1="n"
    ans2="y"
    ans3="y"
    for i in li:
      if n<=360:
        if n%i==0 and n//i in li:
            ans1="y"
            break
      else:
          if n%i==0:
              ans1="y"
              break
    if n==1:
        ans3="n"
    print(ans1,ans2,ans3)



