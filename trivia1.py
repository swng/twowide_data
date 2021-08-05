import requests
import json

#response = requests.get("https://twowi.de/getRush")
#rush = response.json()

totals = []

for j in range(1,101):
        a = open("rushes/getRush" + str(j) + ".json") # have a rushes folder containing all the rush jsons using this name format
        rush = json.load(a)

        total = 0

        for puzzle in rush:
            queue = puzzle['pieces']
            # print(len(queue))
            total = total + 1 + len(queue)

        #print(total)
        totals.append(total)

print(min(totals), max(totals))