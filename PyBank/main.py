#Import Dependencies
import os
import csv

#Specify the file path
file_infor = os.path.join("..", "PyBank", "budget_data.csv")

#Create empty lists to store data
total_months = []
total_profit = []
change_profit_monthly = []

#Open csv file
with open(file_infor, newline="", encoding="utf-8") as csvfile:

    #Store csv content as a variable "csvreader"
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header labels
    header = next(csvreader)

    #Iterate through each row in the csv
    for row in csvreader:

        # Append the total months and total profit to their respective list
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Iterate through the profits and get the monthly change in profits
    for j in range(len(total_profit)-1):

        change_profit_monthly.append(total_profit[j+1]-total_profit[j])

#Calucate the max and min of the monthly profit change
max_increase_value = max(change_profit_monthly)
max_decrease_value = min(change_profit_monthly)


#Correlate max and min to the proper month using month list and index from max and min, +1 month for next month
max_increase_month = change_profit_monthly.index(max(change_profit_monthly)) + 1
max_decrease_month = change_profit_monthly.index(min(change_profit_monthly)) + 1

#Print the Financial Analysis Results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(change_profit_monthly)/len(change_profit_monthly),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#Create outfile path
output_file = os.path.join("..", "PyBank", "Financial_Analysis_Summary.txt")

#Open the output file, in "write"
with open(output_file,"w") as file:

    #Write the results to the new csv fil "Election Results"
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