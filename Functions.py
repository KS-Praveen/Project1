s = input("please enter your string")
d = {}
for x in s:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
print(d)
