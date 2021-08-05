Various python and js scripts involved in collecting twowi.de puzzle rush data

Not associated with the site, this is just a fan project. Collecting these data kinda goes against the spirit of the pure puzzle rush challenge, admittedly.

Each Puzzle Rush, a randomized subset of all the rushes is delivered to the player to play. In short, this project collects a large number of rushes and processes the data with the goal of discovering and documenting (and ultimately solving) all the puzzles.

Filenames are heavily non informative lol. Here's some documentation:

a.py - request a rush and save to some file
/rushes folder contains 100 such downloaded rush data files
b.py - we take ten downloaded getRush files and scan them for newly discovered puzzles
        where getRush.json contains the master list of all already-known puzzles (in the same format as how they are delivered)
        getRush.json is updated; getRushNew.json is populated with the new puzzles
b (old).py - old version. where rushes 1-25 are already processed and you're looking for new puzzles in 26
d.py - do a large number of rush requests and search for undiscovered puzzles
e.py - scan omg.json for newly discovered puzzle
        where getRush.json contains the master list of all already-known puzzles (in the same format as how they are delivered)
        getRush.json is updated; getRushNew.json is populated with the new puzzles

config.json - (hopefully not included) - just contains the token to a discord bot

distribution.py - parse data and generate encounter location distribution histograms for each problem; upload histograms to a discord channel
distribution_fake.py - for newly discovered puzzles without data saved, generate a fake distribution based on winrate

getRush.json - master list of all already-discovered discovered puzzles
getRushNew.json - newly discovered puzzles from a particular passthrough, relative to the master list
omg.json - a temporary getRush file that includes a new puzzle
out.csv - an exported CSV of processed puzzle data (processed from getRush raw data file)
solutions.txt - manually curated fumens of puzzle solutions

stuff.js - process getRushNew.json and post puzzle details to discord
stuff2.js - process getRush.json and generate out.csv of puzzle details

trivia2.py - categorize puzzles into winrate range buckets (difficulty categories)

upload_solutions.js - upload solutions.txt to discord, formatted

------------------------

btw it is known that 372 was adjusted. Manually renamed the old 372 to 3720 and added the new 372