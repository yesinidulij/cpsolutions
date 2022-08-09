# cook your dish here
for _ in range(int(input())):
    li = list(map(str, input().split()))

    if len(li) == 4:
        m = int(li[0]) * 0.5 + int(li[2]) * 0.05
        if len(str(m)) == 3 and str(m)[2] == "0":
            print("Case" + " " + str(_ + 1) + ":", int(m))
        else:
            print("Case" + " " + str(_ + 1) + ":", str(m).strip())
    else:
        m = int(li[0]) * 0.5
        if len(str(m)) == 3 and str(m)[2] == "0":
            print("Case" + " " + str(_ + 1) + ":", int(m))
        else:
            print("Case" + " " + str(_ + 1) + ":", str(m).strip())
