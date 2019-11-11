import os
import csv

file_infor = os.path.join("..", "PyBank", "budget_data.csv")

total_months = []
total_profit = []
change_profit_monthly = []

with open(file_infor, newline="", encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:

        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for j in range(len(total_profit)-1):

        change_profit_monthly.append(total_profit[j+1]-total_profit[j])

max_increase_value = max(change_profit_monthly)
max_decrease_value = min(change_profit_monthly)

max_increase_month = change_profit_monthly.index(max(change_profit_monthly)) + 1
max_decrease_month = change_profit_monthly.index(min(change_profit_monthly)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(change_profit_monthly)/len(change_profit_monthly),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


output_file = os.path.join("..", "PyBank", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(change_profit_monthly)/len(change_profit_monthly),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")