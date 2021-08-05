# scan omg.json for newly discovered puzzle
# where getRush.json contains the master list of all already-known puzzles (in the same format as how they are delivered)

# getRush.json is updated; getRushNew.json is populated with the new puzzles


import json

z = open("getRush.json", "r")
documented = json.load(z)
z.close()

a = open("omg.json", "r")


aData = json.load(a)



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
        


print(len(new))
combined.sort(key = lambda x: x["id"])

temp = [x["id"] for x in combined]
print(sorted(list(set([x for x in range(422)]) - set(temp))))


json.dump(combined, open('getRush.json','w'))
json.dump(new, open('getRushNew.json','w'))

json.dump({"temp":-1}, open('temp.json','w'))