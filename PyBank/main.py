# Import Necessary Tools
import os
import csv

# Initiate File Path
csvpath = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

# List Declaration    
months = []
profit_loss_list = []
monthly_change_list = []
    

# Open File Path
with open(csvpath) as budget:
    csvreader = csv.reader(budget, delimiter = ',')
    
# Get Header
    header = next(csvreader)
    print(f"CSV Header: {header}")
    
    for row in csvreader:
        months.append(row[0])
        profit_loss_list.append(int(row[1]))
        total_months = len(profit_loss_list)
        total = sum(profit_loss_list)
        
# Month Change, Greatest Increase, Greatest Decrease
months_2 = months.copy()
months_2.remove(months[0])

# Create Period Change
delta_1 = profit_loss_list.copy()
delta_1.remove(delta_1[0]) 
    
# Connect Dates
delta_2 = profit_loss_list.copy()
delta_2.remove(delta_2[85])
    
# Combine Lists     
for first_value, second_value in zip(delta_1, delta_2):
    monthly_change_list.append(first_value - second_value)
    mean_change = round(sum(monthly_change_list) / len(monthly_change_list), 2)
    highest_increase = max(monthly_change_list)
    highest_decrease = min(monthly_change_list)
    highest_increase_date = months_2[monthly_change_list.index(highest_increase)]
    highest_decrease_date = months_2[monthly_change_list.index(highest_decrease)]

# Print Results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${mean_change}")
print(f"Greatest Increase in Profits: {highest_increase_date} (${highest_increase})")
print(f"Greatest Decrease in Profits: {highest_decrease_date} (${highest_decrease})")

# Add Results to List For Export
results = ["Financial Analysis", "----------------------------", 
           f"Total Months: {total_months}", f"Total: ${total}", 
           f"Average Change: ${mean_change}", f"Greatest Increase in Profits: {highest_increase_date} (${highest_increase})",
           f"Greatest Decrease in Profits: {highest_decrease_date} (${highest_decrease})"]

# Create Text File With Results
with open("financial_analysis.txt", "w") as f:
    for results in results:
        f.write(results)
        f.write("\n")