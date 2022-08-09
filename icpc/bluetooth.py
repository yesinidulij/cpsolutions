cntlu = 8
cntru = 8
cntll = 8
cntrl = 8
n = int(input())
for i in range(n):
    t, c = map(str, input().split())
    if c == "b":
        if t[0] == "+":
            cntlu = 0
        elif t[0] == "-":
            cntll = 0
        if t[1] == "+":
            cntru = 0
        elif t[1] == "-":
            cntrl = 0
    else:
        if t[0] == "+":
            cntlu -= 1
        elif t[0] == "-":
            cntll -= 1
        if t[1] == "+":
            cntru -= 1
        elif t[1] == "-":
            cntrl -= 1
if (cntlu <= 0 or cntll <= 0) and (cntru <= 0 or cntrl <= 0):
    print("2")
if cntlu > 0 and cntll > 0:
    print("0")
if cntrl > 0 and cntru > 0:
    print("1")
