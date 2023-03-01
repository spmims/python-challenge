# Import Necessary Tools
import csv
import os

# Create File Path
csvpath = os.path.join("python-challenge", "PyPoll", "Resources", "election_data.csv")

# Assigning variable, list, and dictionaries
candidate_names = []
votes = {}
percent = {}
total_votes = 0

with open(csvpath) as voting_file:
    csvreader = csv.reader(voting_file, delimiter = ",")
    


