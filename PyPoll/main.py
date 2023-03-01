#import csv
#import os

#candidate_names = []
#all_candidates = []
#percents =[]
#data_table = []
#total = 0

#csvpath = os.path.join("\\Users\\steph\\Desktop\\Data Analytics and Visualization\\python-challenge\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#with open(csvpath) as voting:
    #csvreader = csv.reader(voting)
    #header = next(csvreader)
    
    #for row in csvreader:    
        #total += 1
    
        #all_candidates.append(row[2]) #appending the vote to all_candidates
        #if row[2] in candidate_names: #matching
            #continue
        #else: #else condition starts
            #candidate_names.append(row[2]) # appending the name of candidates i election
    #total-=1
#for i in range(1,len(candidate_names)): #loop for counting the votes of each candidate
    #count=0 #count variable to store votes count of individual candidate
    #for j in range(len(all_candidates)):
        #if candidate_names[i]==all_candidates[j]:
            #count+=1
    #data_table[candidate_names[i]]=count #inserting the name of candidate and their votes
#candidate_names.remove(candidate_names[0])
            
#print("Election Results")
#print("____________________________\n")
#print("Total Votes: %d"%total) #printing the total votes
#print("____________________________\n")
#for i in candidate_names:
    #percentage=(data_table[i]/total)*100 #finding the percentage of each candidate
    #percents.append(percentage) #appending the precentage to percent_list
#print("%s : %f(%d)"%(i,percentage,data_table[i]))
#print("____________________________\n")
#print("Winner:",candidate_names[percents.index(max(percents))]) #declaring the winner of the election
#print("\t____________________________\n")