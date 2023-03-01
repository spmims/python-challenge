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
    
print(total_votes, candidate_list, votes, max(votes, key = votes.get), percent, sep = "\n")    

# Vote Counting for Each Candidate
voting_counts = {}
for name in candidate_list:
    voting_counts[name] = str(percent[name]) + "% " + "(" + str(votes[name]) + ")"
    
output = "\n".join(f"{key}: {unit}" for key, unit in voting_counts.items())

# Put Results into Format for Sending to File
results = (f"Election Results\n" f"-------------------------\n" f"Total Votes: {total_votes}"
           f"-------------------------\n" f"{output}\n" f"-------------------------\n"
           f"Winner: {max(votes, key = votes.get)}\n" f"-------------------------\n")

