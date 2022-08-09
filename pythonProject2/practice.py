b = "HelloWorld"
a=5
print(str(a).format("{:.2f}"))
#print(b.find('o'))
#print(b.isalpha())
#print(b.casefold())
print(b.swapcase())
fruits=["banana","mango","papaya","apple"]
biscuits=["vanilla","caputino","fegegta","abwoled","strawberry"]
fruits.extend(biscuits)

f=fruits.copy()
f.clear()
print(f)
fruits.append(biscuits)
fruits.insert(4,"inserted")
print(fruits)
[print(x) for x in biscuits if "t" in x]
newBiscuits=["sweet" for x in biscuits]
[print(x) for x in newBiscuits]
newlist = [x if x == "banana" else "orange" for x in fruits]
print(newlist)
