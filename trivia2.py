import json
from matplotlib import pyplot as plt 
import matplotlib
import numpy as np 
import math

a = open("getRush.json") # have a rushes folder containing all the rush jsons using this name format
rush = json.load(a)

groups = [
    [],[],[],[],[],[],[],[],[],[]
]


for puzzle in rush:
    id = puzzle['id']
    w = puzzle['winrate']
    if w == '':
        w = '0.00'

    group = math.floor(float(w) / 10)
    groups[group].append(id)

print('0 to 10%', groups[0])
print('10 to 20%', groups[1])
print('20 to 30%', groups[2])
print('30 to 40%', groups[3])
print('40 to 50%', groups[4])
print('50 to 60%', groups[5])
print('60 to 70%', groups[6])
print('70 to 80%', groups[7])
print('80 to 90%', groups[8])
print('90 to 100%', groups[9])



    
