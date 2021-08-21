def getindices(s):
    return [i for i, c in enumerate(s) if c.isupper()]

somestring = input()

capitals = getindices(somestring)
print(capitals)