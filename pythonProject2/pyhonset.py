#set input
s1=set(input().split())
s2=set(input().split())
print(s1.union(s2))
s1.intersection_update(s2)
print(s1)
print(s1.intersection(s2))
s2.symmetric_difference_update(s1)
print(s2)


