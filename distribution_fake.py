# parse data and generate encounter location distribution histograms for each problem; upload histograms to a discord channel
# for newly discovered puzzles without data saved, generate a fake distribution based on winrate

import discord
import time

import json
from matplotlib import pyplot as plt 
import matplotlib
import numpy as np 

config = open("config.json")
TOKEN = json.load(config)["token"]
client = discord.Client()

master = open("getRush.json")
masterData = json.load(master)

def distribution(i):
    data = []
    for j in range(1,101):
        a = open("rushes/getRush" + str(j) + ".json") # have a rushes folder containing all the rush jsons using this name format
        aData = json.load(a)
        a.close()

        for k in range(len(aData)):
            if aData[k]["id"] == i:
                data.append(k+1)
    if len(data) == 0: # no data! 
        # assume that puzzles appear in decreasing order by winrate and pretend the puzzle appeared in a particular spot
        winrate = -1 # get winrate from master file
        for l in range(len(masterData)):
            if masterData[l]["id"] == i:
                winrate = masterData[l]["winrate"]
        if winrate == -1: # not in master file
            return False
        for j in range(1,101):
            a = open("rushes/getRush" + str(j) + ".json") # have a rushes folder containing all the rush jsons using this name format
            aData = json.load(a)
            a.close()

            found = False
            for k in range(len(aData)):
                if (not found and (aData[k]["winrate"] < winrate)):
                    found = True
                    data.append(k+1)
        

    data_np = np.array(data)
    fig, ax = plt.subplots()
    ax.set_facecolor('#36393E')
    fig.patch.set_facecolor('#36393E')

    plt.hist(data_np, bins = [x for x in range(90)], color='#ED4245') # histogram with fixed bins up to 90, red bars
    plt.title("ID " + str(i), color = '#FFFFFF')
    plt.xlabel('Encounter Location (maybe)', color = '#FFFFFF')
    plt.ylabel('Frequency', color = '#FFFFFF')

    plt.xticks(np.arange(0, 90, 5))

    ax.tick_params(axis='x', colors='#FFFFFF')
    ax.tick_params(axis='y', colors='#FFFFFF')
    

    for child in ax.get_children(): # basically everything here is trying to set everything white
        if isinstance(child, matplotlib.spines.Spine):
            child.set_color('#FFFFFF')
    for child in fig.get_children():
        if isinstance(child, matplotlib.spines.Spine):
            child.set_color('#FFFFFF')


    #plt.show()
    plt.savefig('distribution.png')
    plt.close('all') # otherwise you'll run out of memory after a while
    return True

@client.event                
async def on_ready():
    for id in [197, 229, 168, 320, 230, 341, 400, 21, 83, 106, 235, 74, 41, 328, 100, 377, 181, 205, 61, 342, 60, 68, 372]:
        if distribution(id):
            print(id)
            file = discord.File("distribution.png")
            msg = "ID: " + str(id)
            await client.get_channel(869832185727832085).send(content = msg, file=file) # encounter location channel ID
            time.sleep(3) # please don't rate limit me discord, 3s is reasonable right?
        else:
            print(id, "nope")


client.run(TOKEN)