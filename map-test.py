def rev(source):
    output = ""
    for i in range(len(source)-1, -1, -1):
        output += source[i]
    return output

names = ["walter", "arabella", "shealyn", "ainsley", "elin", "Jason"]

#revnames = list(map(rev, names))
#print(revnames)
print(names)
print(list(map(rev, names)))
print(list(filter(lambda name: len(name) > 5, names)))
