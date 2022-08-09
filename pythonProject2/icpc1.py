from math import ceil

n, s, k, m = map(int, input().split())
minans = ceil((n / s)) * m
maxans = ceil(n * (k + 1) / s) * m
print(minans, maxans)