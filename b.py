# we take ten downloaded getRush files and scan them for newly discovered puzzles
# where getRush.json contains the master list of all already-known puzzles (in the same format as how they are delivered)

# getRush.json is updated; getRushNew.json is populated with the new puzzles


import json

z = open("getRush.json", "r")
documented = json.load(z)
z.close()

a = open("rushes/getRush90.json", "r")
b = open("rushes/getRush91.json", "r")
c = open("rushes/getRush92.json", "r")
d = open("rushes/getRush93.json", "r")
e = open("rushes/getRush94.json", "r")
f = open("rushes/getRush95.json", "r")
g = open("rushes/getRush96.json", "r")
h = open("rushes/getRush97.json", "r")
i = open("rushes/getRush98.json", "r")
j = open("rushes/getRush99.json", "r")
k = open("rushes/getRush100.json", "r")


aData = json.load(a)
bData = json.load(b)
cData = json.load(c)
dData = json.load(d)
eData = json.load(e)
fData = json.load(f)
gData = json.load(g)
hData = json.load(h)
iData = json.load(i)
jData = json.load(j)
kData = json.load(k)



def not_in(puzzle, combined): # dedicated function instead of just using "in" operator because we're specifically checking for ID match (eg completions may be different)
    id = puzzle["id"]
    for match in combined:
        match_id = match["id"]
        if match_id == id:
            return False

    return True


new = []
combined = documented



for puzzle in aData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in bData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in cData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in dData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in eData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in fData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in gData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in hData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in iData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in jData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
for puzzle in kData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)
        


print(len(new))
combined.sort(key = lambda x: x["id"])

temp = [x["id"] for x in combined]
print(sorted(list(set([x for x in range(422)]) - set(temp)))) # check which IDs still have yet to be discovered


json.dump(combined, open('getRush.json','w'))
json.dump(new, open('getRushNew.json','w'))

json.dump({"temp":-1}, open('temp.json','w')) # prepping some config file with an initial value for a later process