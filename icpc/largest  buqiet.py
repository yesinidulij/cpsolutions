for _ in range(int(input())):
    mg, my, mr = map(int, input().split())
    og, oy, ore = map(int, input().split())
    pg, py, pr = map(int, input().split())
    m=max(mg+my+mr,og+oy+ore,pg+py+pr,mg+og+pg,my+oy+py,mr+ore+pr)
    if m%2!=0:
        print(m)
    else:
        print(m-1)
