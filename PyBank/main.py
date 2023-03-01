import os
import csv

# file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# variable declaration
total_profit_losses = 0
last_profit_losses = 0
profit_losses_change = 0
month_change = []
months = []
total_profit = []
profit_loss_change_list = []
greatest_inc = ["", 0]
biggest_increase = 0
biggest_decrease = 9999999999999999

# open csv
with open(csvpath) as budget:
    csvreader = csv.reader(budget)
    header = next(csvreader)
    
    first_row = next(csvreader)
    prev_net = int(first_row[1])
    
    for row in csvreader:
        months.append(row[0])
        total_profit.append(row[1])
        
    total_months = len(months)
    
    #total_profit_losses = total_profit_losses = int(row["Profits/Losses"])
    #profit_losses_change = int(row["Profit/Losses"]) - last_profit_losses
    #profit_loss_change_list.append(profit_losses_change)
    #last_profit_losses = int(row["Profit/Losses"])
    #month_change = month_change = [row["Date"]]
    
    total_profit=[int(y) for y in total_profit] 
    total_profit_sum=sum(total_profit)  
    
    
    
net_change = int(row[1]) - prev_net

if net_change > greatest_inc['',0]:
    greatest_inc[0] = row[0]
    


    #for i in range(len(total_profit)-1):
    #    month_change.append(total_profit[i+1]-total_profit[i])
        
#biggest_increase = max(profit_loss_change_list)
#biggest_decrease = min(profit_loss_change_list)

#biggest_increase_month = profit_loss_change_list.index(biggest_increase) + 1
#biggest_decrease_month = profit_loss_change_list.index(biggest_decrease) + 1

print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_sum}")
print(f"Greatest increase: {greatest_inc}")
#print(f"Average Change: ${biggest_increase_month}")
#print()





#file = "C:\\Users\\steph\\Desktop\\Data Analytics and Visualization\\python-challenge\\python-challenge\\PyBank\\Resources\\budget_data.csv"

#original_df = pd.read_csv(file)
#original_df.head()



# Code for the number of months present in the data set #
#print("Total Months:", len(original_df))

# Code for the total profit/loss #
#print("Total:", original_df['Profit/Losses'].sum())

# Code for changes in profit/losses over the time period and averages#

# Code for greatest increase in profits #
#max_original_df = original_df['Profit/Losses'].max()
#print ("Greatest Increase in Profits:", max_original_df)

#Code for greatest decrease in profits #
#print ("Greatest Decrease in Profits:", original_df['Date'].min(), original_df['Profit/Losses'].min())