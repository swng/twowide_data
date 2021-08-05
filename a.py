# request a rush and save to some file

import requests
import json

response = requests.get("https://twowi.de/getRush")
rush = response.json()

json.dump(rush, open('rushes/getRush100.json','w')) # increment this number to save to a new file each time