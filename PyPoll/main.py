# Import Necessary Tools
import csv
import os

# Create File Path
csvpath = os.path.join("python-challenge", "PyPoll", "Resources", "election_data.csv")

# Assigning variable, list, and dictionaries
candidate_list = []
votes = {}
percent = {}
total_votes = 0

# Read in CSV
with open(csvpath) as voting_file:
    csvreader = csv.reader(voting_file, delimiter = ",")
    
    print(csvreader)
    
# Get Headers
    header = next(csvreader)
    print(f"CSV Header: {header}")
    
# Collect the Votes
    for row in csvreader:
        total_votes = total_votes + 1
    
# Appending List of Candidates and Vote Totals
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            votes[row[2]] = 0
        
        votes[row[2]] += 1
        
    for candidate in candidate_list:
        percent[candidate] = round((votes[candidate] / sum(votes.values())) * 100, 3)
    
    


