import os
import csv

budget_csvpath = os.path.join('Resources', 'budget_data.csv')

#open and read csv
with open(budget_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#variables
months = []
net_profit_loss_changes = []

count_months = 0
net_profit_loss = 0
prior_month_profit = 0
current_month_profit_loss = 0
profit_loss_change = 0

#read header row
csv_header = next(csvfile)

#total # of months
for row in csvreader:

    count_months +=1

#net total of profit and losses
    current_month_profit_loss = int(row[1])
    net_profit_loss += current_month_profit_loss

    if (count_months ==1):
        prior_month_profit = current_month_profit_loss
        continue
    
    else:

    #change in profit loss
        profit_loss_change = current_month_profit_loss - prior_month_profit
    
    months.append(row[0])

    profit_loss_change.append(profit_loss_change)

    prior_month_profit = current_month_profit_loss

#average of profit and losses
sum_profit_loss = sum(profit_loss_change)
avg_profit_loss = round(sum_profit_loss/count_months - 1), 2,

#the greatest increase in profits(date and amount)
highest_change = max(profit_loss_change)
lowest_change = min(profit_loss_change)

#the greatest decrease om losses(date and amount)
highest_month_index = profit_loss_change.index(highest_change)
lowest_month_index = profit_loss_change.index(lowest_change)

best_month = months[highest_month_index]
worst_month = months[lowest_month_index]

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {count_months}")
print(f"Total: {net_profit_loss}")
print(f"Average Change: {avg_profit_loss}")
print(f"Greatest Increase in Profits: {best_month} {highest_change})")
print(f"Greatest Decrease in Profits: {worst_month} {lowest_change})")










    





        



