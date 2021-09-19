import os
import csv

budget_data_csv_path = os.path.join('Resources', 'budget_data.csv')
budget_data_csv_path_out = os.path.join('Resources', 'budget_data.txt')

with open(budget_data_csv_path, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader, None)

    months = 0
    net_pl = 0
    total_pl = 0
    avg_pl_change = 0
    greatest_incr = 0
    greatest_decr = 0

    for row in csvreader:
        months += 1
        total_pl += int(row[1])

        if int(row[1]) - avg_pl_change > greatest_incr:
            greatest_incr = int(row[1]) - avg_pl_change
            greatest_incr_month = row[0]
        elif int(row[1]) - avg_pl_change < greatest_decr:
            greatest_decr = int(row[1]) - avg_pl_change
            greatest_decr_month = row[0]

            net_pl += int(row[1])

        avg_pl_change = int(row[1])


print("Financial Analysis")
print("--------------------")
print(f"Total Months: {months}")
print(f"Total: {net_pl}")
print(f"Average Change: {avg_pl_change}")
print(f"Greatest Increase in Profits: {greatest_incr_month} {greatest_incr})")
print(f"Greatest Decrease in Profits: {greatest_decr_month} {greatest_decr})")
