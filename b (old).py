# old version. where rushes 1-25 are already processed and you're looking for new puzzles in 26

import json

a = open("getRush1.json", "r")
b = open("getRush2.json", "r")
c = open("getRush3.json", "r")
d = open("getRush4.json", "r")
e = open("getRush5.json", "r")
f = open("getRush6.json", "r")
g = open("getRush7.json", "r")
h = open("getRush8.json", "r")
i = open("getRush9.json", "r")
j = open("getRush10.json", "r")
k = open("getRush11.json", "r")
l = open("getRush12.json", "r")
m = open("getRush13.json", "r")
n = open("getRush14.json", "r")
o = open("getRush15.json", "r")
p = open("getRush16.json", "r")
q = open("getRush17.json", "r")
r = open("getRush18.json", "r")
s = open("getRush19.json", "r")
t = open("getRush20.json", "r")
u = open("getRush21.json", "r")
v = open("getRush22.json", "r")
w = open("getRush23.json", "r")
x = open("getRush24.json", "r")
y = open("getRush25.json", "r")
z = open("getRush26.json", "r")




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
lData = json.load(l)
mData = json.load(m)
nData = json.load(n)
oData = json.load(o)
pData = json.load(p)
qData = json.load(q)
rData = json.load(r)
sData = json.load(s)
tData = json.load(t)
uData = json.load(u)
vData = json.load(v)
wData = json.load(w)
xData = json.load(x)
yData = json.load(y)
zData = json.load(z)



def not_in(puzzle, combined): # dedicated function instead of just using "in" operator because we're specifically checking for ID match (eg completions may be different)
    id = puzzle["id"]
    for match in combined:
        match_id = match["id"]
        if match_id == id:
            return False

    return True


new = []
combined = []

# would be simpler to just compare the newest getRush against the full getRush file but uhhh I guess we're going through all the files because because

for puzzle in aData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in bData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in cData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in dData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in eData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in fData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in gData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in hData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in iData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in jData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in kData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in lData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in mData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in nData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in oData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in pData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in qData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in rData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in sData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in tData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in uData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in vData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in wData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in xData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
for puzzle in yData:
    if not_in(puzzle, combined):
        combined.append(puzzle)

for puzzle in zData:
    if not_in(puzzle, combined):
        combined.append(puzzle)
        new.append(puzzle)


print(len(new))
combined.sort(key = lambda x: x["id"])

#temp = [x["id"] for x in combined]
#print(sorted(list(set([x for x in range(422)]) - set(temp))))


json.dump(combined, open('getRush.json','w'))
json.dump(new, open('getRushNew.json','w'))