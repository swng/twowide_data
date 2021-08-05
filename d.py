# search for undiscovered puzzles

import requests
import json
import time

search = [13, 57, 62, 231, 264, 416] # list of IDs not yet discovered

for i in range(100): # request 100 rushes and scan each for undiscovered IDs. Output to omg.json and quit if found.
    response = requests.get("https://twowi.de/getRush")
    rush = response.json()

    for puzzle in rush:
        id = puzzle["id"]
        if id in search:
            print("omg omg omg omg omg omg")
            print(id)
            json.dump(rush, open('omg.json','w'))
            quit()


    time.sleep(1)


print("yep nope nothing in 100 rushes")