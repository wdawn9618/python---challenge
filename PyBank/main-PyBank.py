import os
import csv

budget = os.path.join("budget_data.csv")

#variables
month_chg = []
net_profit = []
date = []

count_months = 0
profit_total = 0
profit_change = 0
profit_pure = 0

#read header row
#csv_header = next(csvfile)
#open and read csv
with open(budget, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)


#total # of months
    for row in reader:
      count_months = count_months + 1

#incr/decr in profits
date.append(row[0])

#calc total profits
net_profit.append(row[1])
profit_total = profit_total + int(row[1])

#change in profit
avg_chg_prof= int(row[1])
chg_profit = avg_chg_prof - profit_pure

month_chg.append(chg_profit)

profit_change = profit_change + chg_profit
profit_pure = avg_chg_prof

average_change = profit_change/count_months

incr_profits = max(month_chg)
decr_profits = min(month_chg)
    
best_month = date[month_chg.index(incr_profits)]
worst_month = date[month_chg.index(decr_profits)]

print("Financial Analysis")
print("--------------------")
print(f"Total Months: " + str(count_months))
print(f"Total Profits: " + "$" + str(profit_total))
print(f"Average Change: " + "$" + str(int(average_change)))
print(f"Greatest Increase in Profits: " + str(best_month) +" ($" + str(incr_profits) + ")")
print(f"Greatest Decrease in Profits: " + str(worst_month) +" ($" + str(decr_profits) +")")
print("--------------------------")










    





        



